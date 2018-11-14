def process_file(file_name):
    names_catalog = [] 
    babes = open("babynames/" + file_name)
    name_catalog = [line.strip('\n').split(',') for line in babes if line != '']
    return name_catalog

def total_births(year):
    analyzed_year = str(year)
    births = 0
    for years in process_file('yob' + analyzed_year + '.txt'):
        births += int(years[2])
    return births

def proportion(name, gender, year):
    analyzed_year = str(year)
    proport = 0
    for years in process_file('yob' + analyzed_year + '.txt'):
        if years[0].lower() == name.lower() and years[1] == gender:
            proport = int(years[2]) / total_births(year)
    return proport


def highest_year(name, gender):
    highest = 0
    largest_year= 0
    for year in range(1880, 2011):
        if proportion(name, gender, year) > highest:
            highest = proportion(name, gender, year)
            largest_year = year
    return largest_year


def main():
    print('Waylon had the highest proportion among male baby names in the year', highest_year('Waylon', 'M'))

if __name__ == '__main__':
    main()