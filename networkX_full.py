import pandas as pd
import networkx as nx
file_name = 'combined'
df1 = pd.read_csv(r'./data/yellow_tripdata_2021-01.csv')
df2 = pd.read_csv(r'./data/yellow_tripdata_2021-02.csv')
df3 = pd.read_csv(r'./data/yellow_tripdata_2021-03.csv')
df4 = pd.read_csv(r'./data/yellow_tripdata_2021-04.csv')
# df = pd.read_csv(r'./data/yellow_tripdata_2021-04.csv')
df= pd.concat([df1,df2,df3,df4])
##distinct ratecode

df['RatecodeID'].value_counts()

##standard rates only
df = df[df['RatecodeID']==1]

##crete a column for trip duration
df['tpep_pickup_datetime_dt'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime_dt'] = pd.to_datetime(df['tpep_dropoff_datetime'])

df['duration'] = df['tpep_dropoff_datetime_dt'] -df['tpep_pickup_datetime_dt']

df['duration'] =df['duration'].apply(lambda x:x.seconds/60)
df['hour'] = df['tpep_pickup_datetime_dt'].apply(lambda x:x.hour)
df['amount'] = df['total_amount'] - df['tip_amount']
from matplotlib import pyplot as plt
df=df[df['amount']>0]
df2 = df[df['duration']<180]
df3 = df2.sort_values(['tip_amount'],ascending=False)

columns_take = ['duration','amount','trip_distance','PULocationID','DOLocationID']
df2=df2[columns_take]

df2=df2[df2['PULocationID']!=df2['DOLocationID']]

df3=df2[(df2['PULocationID']!=265) & (df2['DOLocationID']!=265) ]
df3=df3[(df3['PULocationID']!=264) & (df3['DOLocationID']!=264) ]
df3['count']=1
df3_grouped = df3.groupby(['PULocationID','DOLocationID']).mean().reset_index()
df3_grouped2 = df3.groupby(['PULocationID','DOLocationID']).agg({'amount':'mean', 'duration':'mean','count':'sum','trip_distance':'mean'}).reset_index()
df=df3_grouped2.copy()
dict_x = {1:'Newark Airport',
2:'Jamaica Bay',
3:'Allerton/Pelham Gardens',
4:'Alphabet City',
5:'Arden Heights',6:'Arrochar/Fort Wadsworth',
7:'Astoria',
8:'Astoria Park',
9:'Auburndale',
10:'Baisley Park',
11:'Bath Beach',
12:'Battery Park',
13:'Battery Park City',
14:'Bay Ridge',
15:'Bay Terrace/Fort Totten',
16:'Bayside',
17:'Bedford',
18:'Bedford Park',
19:'Bellerose',
20:'Belmont',
21:'Bensonhurst East',
22:'Bensonhurst West',
23:'Bloomfield/Emerson Hill',
24:'Bloomingdale',
25:'Boerum Hill',
26:'Borough Park',
27:'Breezy Point/Fort Tilden/Riis Beach',
28:'Briarwood/Jamaica Hills',
29:'Brighton Beach',
30:'Broad Channel',
31:'Bronx Park',
32:'Bronxdale',
33:'Brooklyn Heights',
34:'Brooklyn Navy Yard',
35:'Brownsville',
36:'Bushwick North',
37:'Bushwick South',
38:'Cambria Heights',
39:'Canarsie',
40:'Carroll Gardens',
41:'Central Harlem',
42:'Central Harlem North',
43:'Central Park',
44:'Charleston/Tottenville',
45:'Chinatown',
46:'City Island',
47:'Claremont/Bathgate',
48:'Clinton East',
49:'Clinton Hill',
50:'Clinton West',
51:'Co-Op City',
52:'Cobble Hill',
53:'College Point',
54:'Columbia Street',
55:'Coney Island',
56:'Corona',
57:'Corona',
58:'Country Club',
59:'Crotona Park',
60:'Crotona Park East',
61:'Crown Heights North',
62:'Crown Heights South',
63:'Cypress Hills',
64:'Douglaston',
65:'Downtown Brooklyn/MetroTech',
66:'DUMBO/Vinegar Hill',
67:'Dyker Heights',
68:'East Chelsea',
69:'East Concourse/Concourse Village',
70:'East Elmhurst',
71:'East Flatbush/Farragut',
72:'East Flatbush/Remsen Village',
73:'East Flushing',
74:'East Harlem North',
75:'East Harlem South',
76:'East New York',
77:'East New York/Pennsylvania Avenue',
78:'East Tremont',
79:'East Village',
80:'East Williamsburg',
81:'Eastchester',
82:'Elmhurst',
83:'Elmhurst/Maspeth',
84:'Eltingville/Annadale/Princes Bay',
85:'Erasmus',
86:'Far Rockaway',
87:'Financial District North',
88:'Financial District South',
89:'Flatbush/Ditmas Park',
90:'Flatiron',
91:'Flatlands',
92:'Flushing',
93:'Flushing Meadows-Corona Park',
94:'Fordham South',
95:'Forest Hills',
96:'Forest Park/Highland Park',
97:'Fort Greene',
98:'Fresh Meadows',
99:'Freshkills Park',
100:'Garment District',
101:'Glen Oaks',
102:'Glendale',
103:'Governors Island/Ellis Island/Liberty Island',
104:'Governors Island/Ellis Island/Liberty Island',
105:'Governors Island/Ellis Island/Liberty Island',
106:'Gowanus',
107:'Gramercy',
108:'Gravesend',
109:'Great Kills',
110:'Great Kills Park',
111:'Green-Wood Cemetery',
112:'Greenpoint',
113:'Greenwich Village North',
114:'Greenwich Village South',
115:'Grymes Hill/Clifton',
116:'Hamilton Heights',
117:'Hammels/Arverne',
118:'Heartland Village/Todt Hill',
119:'Highbridge',
120:'Highbridge Park',
121:'Hillcrest/Pomonok',
122:'Hollis',
123:'Homecrest',
124:'Howard Beach',
125:'Hudson Sq',
126:'Hunts Point',
127:'Inwood',
128:'Inwood Hill Park',
129:'Jackson Heights',
130:'Jamaica',
131:'Jamaica Estates',
132:'JFK Airport',
133:'Kensington',
134:'Kew Gardens',
135:'Kew Gardens Hills',
136:'Kingsbridge Heights',
137:'Kips Bay',
138:'LaGuardia Airport',
139:'Laurelton',
140:'Lenox Hill East',
141:'Lenox Hill West',
142:'Lincoln Square East',
143:'Lincoln Square West',
144:'Little Italy/NoLiTa',
145:'Long Island City/Hunters Point',
146:'Long Island City/Queens Plaza',
147:'Longwood',
148:'Lower East Side',
149:'Madison',
150:'Manhattan Beach',
151:'Manhattan Valley',
152:'Manhattanville',
153:'Marble Hill',
154:'Marine Park/Floyd Bennett Field',
155:'Marine Park/Mill Basin',
156:'Mariners Harbor',
157:'Maspeth',
158:'Meatpacking/West Village West',
159:'Melrose South',
160:'Middle Village',
161:'Midtown Center',
162:'Midtown East',
163:'Midtown North',
164:'Midtown South',
165:'Midwood',
166:'Morningside Heights',
167:'Morrisania/Melrose',
168:'Mott Haven/Port Morris',
169:'Mount Hope',
170:'Murray Hill',
171:'Murray Hill-Queens',
172:'New Dorp/Midland Beach',
173:'North Corona',
174:'Norwood',
175:'Oakland Gardens',
176:'Oakwood',
177:'Ocean Hill',
178:'Ocean Parkway South',
179:'Old Astoria',
180:'Ozone Park',
181:'Park Slope',
182:'Parkchester',
183:'Pelham Bay',
184:'Pelham Bay Park',
185:'Pelham Parkway',
186:'Penn Station/Madison Sq West',
187:'Port Richmond',
188:'Prospect-Lefferts Gardens',
189:'Prospect Heights',
190:'Prospect Park',
191:'Queens Village',
192:'Queensboro Hill',
193:'Queensbridge/Ravenswood',
194:'Randalls Island',
195:'Red Hook',
196:'Rego Park',
197:'Richmond Hill',
198:'Ridgewood',
199:'Rikers Island',
200:'Riverdale/North Riverdale/Fieldston',
201:'Rockaway Park',
202:'Roosevelt Island',
203:'Rosedale',
204:'Rossville/Woodrow',
205:'Saint Albans',
206:'Saint George/New Brighton',
207:'Saint Michaels Cemetery/Woodside',
208:'Schuylerville/Edgewater Park',
209:'Seaport',
210:'Sheepshead Bay',
211:'SoHo',
212:'Soundview/Bruckner',
213:'Soundview/Castle Hill',
214:'South Beach/Dongan Hills',
215:'South Jamaica',
216:'South Ozone Park',
217:'South Williamsburg',
218:'Springfield Gardens North',
219:'Springfield Gardens South',
220:'Spuyten Duyvil/Kingsbridge',
221:'Stapleton',
222:'Starrett City',
223:'Steinway',
224:'Stuy Town/Peter Cooper Village',
225:'Stuyvesant Heights',
226:'Sunnyside',
227:'Sunset Park East',
228:'Sunset Park West',
229:'Sutton Place/Turtle Bay North',
230:'Times Sq/Theatre District',
231:'TriBeCa/Civic Center',
232:'Two Bridges/Seward Park',
233:'UN/Turtle Bay South',
234:'Union Sq',
235:'University Heights/Morris Heights',
236:'Upper East Side North',
237:'Upper East Side South',
238:'Upper West Side North',
239:'Upper West Side South',
240:'Van Cortlandt Park',
241:'Van Cortlandt Village',
242:'Van Nest/Morris Park',
243:'Washington Heights North',
244:'Washington Heights South',
245:'West Brighton',
246:'West Chelsea/Hudson Yards',
247:'West Concourse',
248:'West Farms/Bronx River',
249:'West Village',
250:'Westchester Village/Unionport',
251:'Westerleigh',
252:'Whitestone',
253:'Willets Point',
254:'Williamsbridge/Olinville',
255:'Williamsburg (North Side)',
256:'Williamsburg (South Side)',
257:'Windsor Terrace',
258:'Woodhaven',
259:'Woodlawn/Wakefield',
260:'Woodside',
261:'World Trade Center',
262:'Yorkville East',
263:'Yorkville West',
264:'NV',
265:'NA'}

# df['PULocationID']=df['PULocationID'].apply(lambda x : dict_x.get(x))
# df['DOLocationID']=df['DOLocationID'].apply(lambda x : dict_x.get(x))
G=nx.from_pandas_edgelist(df, 'PULocationID', 'DOLocationID', [ 'amount', 'duration', 'count','trip_distance'])


# nx.draw(G)

G.degree()
max(dict(G.degree()).items(), key = lambda x : x[1])

degrees_df = pd.DataFrame.from_dict(dict(G.degree),orient='index').reset_index()
degrees_df.columns = ['index','count']
degrees_df = degrees_df.sort_values(['count'],ascending=False)
degrees_df['zone'] = degrees_df['index'].apply(lambda x : dict_x.get(x))
degrees_df.to_csv(f'degrees_connected_{file_name}.csv',index=None)


###shortest path example, 108- 15
G=nx.from_pandas_edgelist(df, 'PULocationID', 'DOLocationID', [ 'amount', 'duration', 'count','trip_distance'], create_using=nx.DiGraph())
nx.shortest_path(G,source=55, target=15,weight='trip_distance')
nx.shortest_path(G,source=55, target=15,weight='duration')
nx.shortest_path(G,source=55, target=15,weight='amount')