import csv


def main():
    all_andro = {}

    for i in range(1880, 2014):
        file_name = 'raw_data/yob' + str(i) + '.csv'
        with open(file_name) as f:
            m_names = {}
            f_names = {}
            total_female_count = 0
            total_male_count = 0
            total_female_andro_count = 0
            total_male_andro_count = 0

            r = csv.reader(f)
            r.next()
            for row in r:
                if row[1] == 'F':
                    f_names[row[0]] = row[2]
                    total_female_count += int(row[2])
                else:
                    m_names[row[0]] = row[2]
                    total_male_count += int(row[2])

            for name in set(f_names.keys()).intersection(set(m_names.keys())):
                percent_female = int(f_names[name]) / (float(m_names[name]) + float(f_names[name]))
                if percent_female > .4 and percent_female < .6:
                    total_female_andro_count += int(f_names[name])
                    total_male_andro_count += int(m_names[name])
            female_andro_percent = (100.0 * total_female_andro_count) / total_female_count
            male_andro_percent = (100.0 * total_male_andro_count) / total_male_count
            total_m_f_ratio_centered = 1.0*total_male_count / total_female_count - 1
            print str(i) + " " + str(total_m_f_ratio_centered)
            all_andro[i] = (female_andro_percent, male_andro_percent)
    print all_andro

if __name__ == '__main__':
    main()
