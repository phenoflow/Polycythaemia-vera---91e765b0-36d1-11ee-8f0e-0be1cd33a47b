# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"B671.00","system":"readv2"},{"code":"B671.11","system":"readv2"},{"code":"B934.12","system":"readv2"},{"code":"16922.0","system":"med"},{"code":"2481.0","system":"med"},{"code":"36790.0","system":"med"},{"code":"37468.0","system":"med"},{"code":"5542.0","system":"med"},{"code":"58888.0","system":"med"},{"code":"63653.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('polycythaemia-vera-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["polycythaemia-vera---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["polycythaemia-vera---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["polycythaemia-vera---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
