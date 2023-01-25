import geocoder
import csv

def line_needs_update(line):
    if len(line) < 8:
        return True

    # LAT / LNG / ADDRESS / COUNTRY / COUNTRY_CODE / COUNTRY_ID / CONTINENTCODE
    if line[2] == "" or line[3] == "" or line[4] == "" or line[5] == "" or line[6] == "" or line[7] == "":
        return True

    if line[2] == 'None' or line[3] == 'None' or line[4] == 'None' or line[5] == 'None' or line[6] == 'None' or line[7] == 'None' or line[8] == 'None':
        return True

    return False

new_file = ""
# open atlas_locations.txt as tsv file
with open('data/atlas_locations_cop.tsv', encoding='utf-8') as tsv_file:
    tsv_file = csv.reader(tsv_file, delimiter="\t")
    for line in tsv_file:
        if len(line) < 2:
            print("Invalid line (Removed): ", line)
        else:
            try:
                if line_needs_update(line):
                    print("Updating:  ", line[0])
                    gnd = int(line[1])
                    g = geocoder.geonames(gnd, method='details', key='lkas')
                    new_line = f"{line[0]}\t{line[1]}\t{g.lat}\t{g.lng}\t" \
                                   f"{g.address}\t{g.country}\t{g.country_code}\t{g.country_geonames_id}\t{g.continent}"
                else:
                    print("Ignored (Up-to-date): ", line)
                    new_line = f"{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}\t" \
                                   f"{line[4]}\t{line[5]}\t{line[6]}\t{line[7]}\t{line[8]}"

                new_file += new_line + "\n"
            except ValueError:
                print("Invalid GND (Removed): ", line)

with open('data/bscc_atlas_locations.tsv', 'w', encoding='utf-8') as updated_file:
    updated_file.write(new_file)