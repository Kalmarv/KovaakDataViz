import csv
import os
import datetime
import pandas as pd

path = "/mnt/d/SteamLibrary/steamapps/common/FPSAimTrainer/FPSAimTrainer/stats/"
dir_list = os.listdir(path)
filenames = [path + i for i in dir_list]
data = []
headers = []

def open_csv(file):
    with open(file, newline='') as f:
        reader = csv.reader(f)
        for i, line in enumerate(reader):
            if len(line) > 5 or line == []:
                if len(line) == 6:
                    if int(line[1]) > 0:
                        data.append(['Date', datetime.datetime.fromtimestamp(os.path.getctime(file)).isoformat()])
                        data.append(['Shots', line[1]])
                        data.append(['Hits', line[2]])
                        data.append(['Accuracy', int(line[2])/int(line[1])])
                        data.append(['Damage Done', line[3]])
                        data.append(['Damage Possible', line[4]])
                    else:
                        del line
            else:
                data.append(line)

for i in filenames:
    open_csv(i)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

stats = []

for i in data:
    stats.append(i[1])

def create_csv(name='master.csv'):
    with open(name, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        headers = []
        for i in data:
            headers.append(i[0])
        writer.writerow(headers[:38])
        for i in chunks(stats, 38):
            writer.writerow(i)

def update_csv(name='master.csv'):
    df = pd.read_csv('master.csv')
    df.drop([
        'Deaths:', 'Fight Time:', 'Damage Taken:', 'Midairs:',
        'Midaired:', 'Directs:', 'Directed:', 'Reloads:',
        'Distance Traveled:', 'Challenge Start:', 'Pause Count:', 'Pause Duration:',
        'Hide Gun:', 'Crosshair:', 'Crosshair Scale:', 'Crosshair Color:'], axis=1, inplace=True)
    df['Score Relative to Average'] = df['Score:']/(df.groupby('Scenario:')['Score:'].transform('mean'))
    df['Score Relative to First Run'] = df['Score:']/(df.groupby('Scenario:')['Score:'].transform('min'))
    df['Accuracy Relative to Average'] = df['Accuracy']/(df.groupby('Scenario:')['Accuracy'].transform('mean'))
    df['Accuracy Relative to First Run'] = df['Accuracy']/(df.groupby('Scenario:')['Accuracy'].transform('min'))
    df['Order'] = df.groupby('Scenario:').cumcount() + 1
    df['Index'] = range(1, len(df) + 1)
    df.rename(columns={'Horiz Sens:': 'Sensitivity', 'Score:': 'Score'}, inplace=True)
    df.to_csv(name, index=False)

create_csv()
update_csv()