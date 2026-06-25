# eu-cbm-hat_jrc_technical_report

> Извлечено из `eu-cbm-hat_jrc_technical_report.pdf` (.pdf).


## Стр. 1

 
The JRC Forest Carbon Model:           
description of EU-CBM-HAT 
 
 
 
 
Blujdea V.N.B., Rougieux P., Sinclair L., Morken S., 
Pilli R., Grassi G., Mubareka S., Kurz W.A. 
 
 
 
2022 
EUR 31299 EN 
ISSN 1831-9424

## Стр. 2

This publication is a Technical report by the Joint Research Centre (JRC), the European Commission’s science and knowledge service. It 
aims to provide evidence-based scientific support to the European policymaking process. The contents of this publication do not 
necessarily reflect the position or opinion of the European Commission. Neither the European Commission nor any person acting on 
behalf of the Commission is responsible for the use that might be made of this publication. For information on the methodology and 
quality underlying the data used in this publication for which the source is neither Eurostat nor other Commission services, users should 
contact the referenced source. The designations employed and the presentation of material on the maps do not imply the expression of 
any opinion whatsoever on the part of the European Union concerning the legal status of any country, territory, city or area or of its 
authorities, or concerning the delimitation of its frontiers or boundaries. 
 
  
 
EU Science Hub 
https://joint-research-centre.ec.europa.eu 
 
 
   JRC130609 
 
   EUR 31299 EN 
 
PDF 
ISBN 978-92-76-58867-2 
ISSN 1831-9424 
doi:10.2760/244051 
KJ-NA-31-299-EN-N 
 
Luxembourg: Publications Office of the European Union, 2022 
 
© European Union, 2022 
 
 
 
 
 
 
The reuse policy of the European Commission documents is implemented by the Commission Decision 2011/833/EU of 12 December 
2011 on the reuse of Commission documents (OJ L 330, 14.12.2011, p. 39). Unless otherwise noted, the reuse of this document is 
authorised under the Creative Commons Attribution 4.0 International (CC BY 4.0) licence (https://creativecommons.org/licenses/by/4.0/). 
This means that reuse is allowed provided appropriate credit is given and any changes are indicated.  
 
 
For any use or reproduction of photos or other material that is not owned by the European Union/European Atomic Energy Community, 
permission must be sought directly from the copyright holders. All content © European Union, 2022, except: cover photo © Viorel N.B. 
Blujdea. 
 
 
How to cite this report: Blujdea, V.N.B., Rougieux, P., Sinclair, L., Morken, S., Pilli, R., Grassi, G., Mubareka, S. and Kurz, A., W., The JRC Forest 
Carbon Model: description of EU-CBM-HAT. Publications Office of the European Union, Luxembourg, 2022. doi:10.2760/244051. 
JRC130609.

## Стр. 3

i 
Contents 
Abstract.....................................................................................................................................................1 
Acknowledgements ....................................................................................................................................2 
1 Introduction ..........................................................................................................................................3 
2 Mandate to develop a transparent, reproducible and open-source forest carbon model ............................4 
2.1 State-of-the-art in forest management and climate policy-oriented modelling .................................4 
2.2 Main development features of EU-CBM-HAT ...................................................................................4 
2.3 EU-CBM-HAT software packages ....................................................................................................6 
3 EU-CBM-HAT architecture: combination of scenarios by “COMBO” ............................................................7 
3.1 Upper level of the EU-CBM-HAT: input information common at EU level ...........................................7 
3.2 Lower level of the EU-CBM-HAT: country specific inputs ..................................................................8 
3.3 Directory “common”: information applicable to all events ............................................................. 10 
3.4 Directory “silv”: description of silvicultural practices, factors for roundwood destination, for volume to 
biomass conversion and market modifiers .......................................................................................... 10 
3.5 Directory “config”: mapping simulation assumptions to generalized assumptions .......................... 14 
3.6 Directory “activities”: input data describing disturbance events ..................................................... 14 
3.6.1 
Defining simulations regarding the conversion to forests ................................................... 15 
3.6.2 
Defining simulations regarding the conversions from forests ............................................. 16 
3.6.3 
Defining simulations regarding the natural disturbances .................................................... 16 
3.6.4 
Defining simulations regarding forest management .......................................................... 17 
3.7 EU-CBM-HAT outputs .................................................................................................................. 18 
3.8 Exploration of EU-CBM-HAT results ............................................................................................. 21 
3.9 Creating a new combination of scenarios .................................................................................... 21 
4 Distribute the expected harvest: harvest allocation tool (HAT) .............................................................. 23 
4.1 HAT concept ............................................................................................................................... 23 
4.2 Treatment of salvage logging ..................................................................................................... 25 
4.3 Distribution of the industrial roundwood and fuelwood harvests ................................................... 25 
4.4 Uncertainty and inconsistency in distributing the harvests ............................................................ 28 
5 Calibration ......................................................................................................................................... 30 
6 Automatic checks of the input data and error messages during the runs............................................... 31 
7 Conclusions ....................................................................................................................................... 32 
References ............................................................................................................................................. 33 
List of abbreviations and definitions ........................................................................................................ 36 
List of figures ......................................................................................................................................... 38 
List of tables .......................................................................................................................................... 39 
Annexes.................................................................................................................................................. 40 
Annex 1. EU-CBM-HAT installation instructions .................................................................................... 40 
Annex 2. Own test of consistency of libcbm and cbm-cfs3 ................................................................... 40

## Стр. 4

1 
Abstract 
The forest carbon model EU-CBM-HAT enables the assessment of forests CO2 emissions and removals under 
scenarios of forest management, natural disturbances, forest-related conversions and roundwood 
destinations (industrial roundwood and fuelwood). This model provides for a rule-based harvest distribution 
based on standing availability in each time step simulated, i.e. status of forest, and applicable silvicultural 
practices, e.g. eligible age range, periodicity, intervention intensity. eu_cbm_hat core package integrates three 
packages: libcbm (as a C++ rewrite of CBM-CFS3 Version 1.2) as the forest growth and disturbances simulator 
(developed by Forest Carbon Accounting team of the Canadian Forest Service), “COMBO”, as the tool for 
combination of scenarios, and “HAT”, as the harvest allocation tool (both in Python, developed by the JRC). The 
eu_cbm_hat is open-source (released and maintained by the JRC), with a dependency to open-source libcbm 
(released and maintained by CFS). The development incorporated into EU-CBM-HAT provides for an increased 
transparency of the modelling chain for forest-related applications associated with GHG reporting and 
mitigation strategies. The model was designed to support policy formulation, implementation and evaluation 
as well as scientific investigations. This report provides both for the scientific background behind the 
development and the user guidance (building on CBM-CFS3 user’s guide).

## Стр. 5

2 
Acknowledgements 
This work was funded by European Commission, DG Research and Innovation under the Administrative 
Agreement DG RTD N° 013 KCB (LC-01591551) JRC Reference N ° 35895 NFP and DG Clima under the 
Administrative Agreement N° JRC.35608 / DG CLIMA N° 340201/2019/815658/AA/CLIMA.C.3. Natural 
Resources Canada developed libcbm and supported the EU-CBM-HAT development by in-kind contributions of 
Scott Morken and Werner A. Kurz. 
Authors 
Viorel N.B. Blujdea, Paul Rougieux, Roberto Pilli, Giacomo Grassi, Sarah Mubareka from European Commission, 
Joint Research Centre, Directorate D – Sustainable Resources, Bioeconomy Unit, Ispra(VA), Italy. 
Scott Morken and Werner A. Kurz from Forest Carbon Accounting Team of the Canadian Forest Service, 
Natural Resources Canada, Victoria, British Columbia, Canada. 
Lucas Sinclair from Sinclair.Bio/Bioinformatics and data science consulting, Geneva, Switzerland.

## Стр. 6

3 
1 Introduction  
Consistent with the EU on climate law, the JRC mandate includes the analysis of the historical sink and future 
GHG mitigation potential of the European forests, forestry and forest sector, under different socio-economic 
scenarios, management systems, wood use, and possibly, climatic conditions. Consequently, an EU forest 
carbon model, called EU-CBM-HAT, was developed by the JRC to support policy formulation, implementation 
and ex post-evaluation when forest, forestry and forest sector are relevant. Scientific investigations can be 
easily implemented given the unlimited combinations of scenarios and freedom to organize the inputs and 
process the outputs. EU-CBM-HAT enables the assessment of forest CO2 emissions and removals from 
forestland and its conversions under different scenarios of forest management and natural disturbances, 
while accommodates scenarios on major categories of roundwood use. It can link to any other model. 
The purpose of this technical report is to provide the scientific background for the methodology behind the 
development of the EU-CBM-HAT and to provide guidance on how to use it. Noteworthy, users must be well 
aware on CBM-CFS3 User’s Guide (Kull et al., 2019). With this report, we aim to increase the transparency 
along the modelling chain and to support further applications from stakeholders for GHG emissions and 
removals estimation, reporting and accounting and for simulating different forest management and climate 
change mitigation scenarios. 
With the scientific needs toward an enhanced support for the development and implementation of EU policies 
related to overall climate neutrality and forests in mind, in the model’s development process, the authors 
focused on following objectives throughout the model’s development process: 
1. to serve the EU climate, bioeconomy, land-use, energy and environmental policies through improved 
modelling of forest processes specific to forests ecosystems, forest management and forestry sector 
(i.e. standing stock increment and forest growth, silvicultural practices, main roundwood destinations). 
2. to improve the transparency and reproducibility of scenarios, assumptions and data from input to 
output, as well as the interoperability with other models both for the forest sector (e.g. harvested 
wood products, wood recycling) or economy wide (e.g. substitution with wood, bioenergy needs). 
3. to promote climate and forestry communities with consistent and versatile information on CO2 
emissions and volume estimates, by addressing equally the climate change community which 
operates with GHG information, i.e. biomass and carbon stocks and stock change and GHG related 
obligations like time bounded referenced periods and specific year targets, and forestry community, 
i.e. operating with forestry’s volume related indicators like standing stock, increment and roundwood 
harvest. 
4. to package the model so that it can run on cloud platforms and operate within the JRC integrated 
modelling framework in support of EU policy making or scientific activities.

## Стр. 7

4 
2 Mandate to develop a transparent, reproducible and open-source forest 
carbon model 
2.1 State-of-the-art in forest management and climate policy-oriented 
modelling 
The forest carbon (C) dynamics can be quantified using empirical models, driven by data provided from forest 
inventories i.e. national forest inventories (NFI) or process-based models, which in turn are driven by the 
simulation of tree and stand physiological and ecological processes and environmental features (e.g. climate, 
geography). Typically, the empirical models are standing stock and increment volume oriented, with simple 
extensions to greenhouse gas (GHG) applications and are best suited for modelling the medium- to short-term 
evolution of the forest C sink under different management strategies (Böttcher et al. 2008) at national scale. 
In modelling capabilities, additional to temporal effect of the mitigation efforts the inclusiveness of all GHG 
sources is key (e.g. Vestin et al., 2022). By simulating the forest growth based on past observations, these 
models cannot easily determine the potential variations in primary productivity induced by climate change on 
the short term (Cuddington et al., 2013). On the other hand, modelling the long-term evolution of the forest 
carbon sink under climate change conditions generally requires the use of process-based climate models, 
grounded in ecological theories, and meaningful validation. These models however, generally miss detailed 
information on management practices and forest conditions, as determined from direct field measurements 
(Pretzsch et al. 2008).  
The European Union (EU) promotes and implements various forest-related policy and strategies which are 
expected to return a European and global benefit, i.e. on climate (e.g. EU climate law, EU LULUCF Regulation 
841/2018, EU forestry strategy) and on environment (Natura 2000 network, a bioeconomy for Europe, EU 
biodiversity strategy for 2030). EU member countries also need models to project forest resources dynamic 
and how they contribute to implementation of EU and national commitments and development. Many 
countries developed their own models (Packalen et al., 2014; Vizzarri et. al, 2021) or applied internationally 
available models, such as EFISCEN (Verkerk et al., 2016) and EFISCEN-space (e.g. Arets and Schelhaas, 2019), 
or the CBM-CFS3 (Kurz et al., 2009). CBM-CFS3 is applied at country level (i.e. bottom-up approach built on 
most detailed data, e.g. from NFI plots), like in: Ireland (Duffy et al., 2021), Czech Republic (Ministry of 
Agriculture et al., 2018), Romania (e.g. Blujdea et al., 2021)., Poland (Ministry of Climate, 2018), Slovenia (e.g. 
Jevšenak et al., 2020). The CBM-CFS3 is an inventory-based, yield-data driven model that simulates the 
stand- and landscape-level C dynamics of above- and belowground biomass, dead wood, litter and soil (Kurz 
et al., 2009).  
The JRC has almost a decade of experience in using the CBM-CFS3 at EU (i.e. top-down approach building on 
aggregate data reported by NFIs, including remote sensing). In support of EU policy, it was applied to 25 MSs, 
based on a specific parametrization of the original model’s assumption, on the EU administrative, ecological 
and silvicultural conditions (e.g. Pilli et al., 2018). The results were validated by a large number of publications 
and science reports (e.g. Pilli et al., 2013; Pilli et al., 2022). Continuity in using such an empirical and stand-
based model by the JRC in support for the EU policies is justified by the type of data publicly available under 
current EU forest monitoring and reporting frameworks.   
During recent years, the JRC has also integrated CBM-CFS3 with numerous other models, e.g. Land-Use based 
Integrated Sustainability Assessment modelling platform (LUISA, e.g. Baranzelli et al., 2014); Global Forest 
Trade Model (GFTM, Jonsson et al., 2015; Rinaldi et al., 2015; Camia et al., 2018; Jonsson et al., 2021), Policy 
Oriented Tool for Energy and Climate Change Impact Assessment (POTEnCIA, European Commission; 2016; 
Mantzos et al., 2016) and CAPRI (Common Agricultural Policy Regional Impact Analysis (CAPRI Modelling 
System, 2022) in an effort toward an integrated modelling framework including the forest-based bioeconomy 
(Mubareka et al., 2014, Mubareka et al., 2018; Sahoo et al., 2021).  
The evolving JRC modelling framework, as a whole, is defining the standard in data processing, as 
continuously evolving components move toward updated open-source programming languages, implicitly 
embraced by the JRC forest-related modelling tools. 
2.2 Main development features of EU-CBM-HAT 
Here we describe the software and programming changes needed to develop EU-CBM-HAT as an open-source 
Python package. Some parts of the development have been implemented by the Canadian Forest Service 
(CFS) while other parts were implemented at the JRC. The Canadian Forest Service developed a new

## Стр. 8

5 
implementation of CBM (short of CBM-CFS3), in the form of a software package called libcbm. Starting from 
this package, the JRC has developed two modules, a Scenario Combination Tool, called COMBO, and a Harvest 
Allocation Tool, called HAT. The three packages were integrated within a unique modelling framework, named 
EU-CBM-HAT. 
Despite the success in supporting policy making by CBM-CFS3 (Grassi et al., 2018), the interoperating of CBM-
CFS3 with other models has been partially limited not only from the lack of a common base scenario and 
background assumptions, but also because of technical restrictions. Up to now, the CBM-CFS3, configured for 
EU, was operated through Microsoft Access graphical user interface which is well suited to calibrate and run 
individual countries and forestry activities independently, but configuring activities integrated and multiple 
models runs for all countries at the EU level was quite complex making it hard to reproduce many scenarios 
with slight variations of the input data. Weak tracking of the assumptions and processing of both the inputs 
and outputs was also difficult as multiple software were involved in various steps. 
The main development targeted by EU-CBM-HAT was the capability to document, automate and reproduce 
model runs. At the start of the project, we evaluated the option to use either the CBM-CFS3 version or the new 
implementation called libcbm. The CBM-CFS3 is well suited for individual use on a desktop computer, and it is 
constantly updated to the new carbon accounting standards, but it is based on an aging software stack. Its 
components make it harder to debug data issues which are likely to arise when working with 27 countries 
simultaneously, numerous administrative regions, non-standard categorization of nationally available data 
and along the other dimensions of the data. Issues can lead to errors inside the different software layers of 
the model such as the Standard Import Tool, the core of the model or the Microsoft Access databases. When 
an error was returned by one component, we lacked the capability to move up and down the software stack to 
understand the context of the error. Also, CBM-CFS3 cannot run on Linux-based cloud platforms and therefore 
limits the interaction with other JRC models to which the forestry model shall plug in. To overcome these 
limitations, the JRC has been testing libcbm since 2020. EU-CBM-HAT is conceptually based on the same 
modelling theory and input data used by CBM-CFS3, but running on a more flexible system. The libcbm is a 
translation of the model to a modern programming language (a C++ core with a Python interface). A section 
below on software provides more details on the components and data formats. This package provides a 
streamlined installation (Annex 1), better error reporting and interoperating features with other software 
packages in the Python ecosystem. 
The second most fundamental development was targeting an increased interoperability of the forest 
management model with other models, e.g. energy model like POTEnCIA formulating fuelwood demands to 
the forestry sector, etc. Based on our previous experience, implementing different scenarios within the CBM-
CFS3 model was extremely time consuming, involving repetitive iterations on the harvest level, especially for 
projections on long periods. Indeed, we could combine different harvest levels with various possible 
management strategies and future afforestation rates (see for example Pilli et al., 2016), as well as potential 
impact of natural disturbances and climate change, as estimated from different climatic models (see Pilli et 
al., 2022). To improve the reproducibility of scenario runs we wanted a directory structure that stores model 
input and output data, in a way that scenarios can be retrieved, modified, mixed and re-run. We wanted to 
keep track of different run versions for comparison purposes. Such traceability also helps to standardize 
model output, in a way that is more reusable by other models. With this purpose in mind, we developed 
COMBO, further integrated with HAT. COMBO allows a flexible association of different forest events, such as 
natural disturbances, and activities, such as forest management practices and pre-defined roundwood use as 
industrial roundwood (IRW) and fuelwood (FW). This is achieved by splitting the different activities in separate 
input files, which are then combined back into a single disturbances input file later sent to libcbm for actual 
run. A combination of scenarios has a name and is described by a configuration file that allows to mix 
different activities, and to change any input parameter programmatically. Furthermore, to keep consistency 
within the JRC integrated modelling framework, the “demand” represents the consumption of roundwood and 
other wood types from domestic harvest, imports and exports. Thus, country’s expected production of 
roundwood represents the domestic harvest, on short “harvest” throughout this report and associated scripts.     
A third development was ensuring an annual time step and rule-based distribution of roundwood harvest. 
Within the CBM-CFS3 version, the allocation of harvest and other disturbance events was based on an expert 
based and iterative process, which was targeting the total harvest defined for the entire simulation period at 
the beginning of the simulation. In particular, before running CBM-CFS3, the expected amount of harvest, as 
defined from historical data sources or different economic models, was preliminary distributed between 
industrial roundwood and fuelwood, and further attributed to each disturbance event applied within the model 
run (including salvage logging and any other management practice) for the entire projected period, as defined 
for each forest type, based on (i) the age structure (used to estimate the clear cut amount), (ii) additional

## Стр. 9

6 
assumptions on the amount of thinnings and (iii) the total C stock available for each stand, according to the 
output provided by a preliminary model run (see Pilli et al., 2013). In this way, the amount of harvest not 
provided from clearcut or salvage logging was further distributed according to the proportion of standing C 
stock available at each step of the simulation, for each disturbance event, forest type and region. This 
approach allowed us to model different management systems (including uneven-aged forests) and to 
calibrate the harvest as a function of the expected amount of wood supply. However, the calibration of the 
main parameters defining each silvicultural event (e.g. overall intensity, definition of the disturbance matrix, 
etc.) sometimes was very cumbersome, e.g. consisting in partial running and successive iterations. Moreover, 
when preliminary distributing the amount of harvest between different disturbance events, the final use of 
the resulting amount of roundwood was attributed to IRW or FW post-simulation. Some difficulties also arose 
from the fact that the harvest was generally specified in terms of volume, but natural disturbances and clear-
cuts are more often specified in terms of area. Finally, when the harvest expected from input data was not 
satisfied, there were no error messages, but additional processing was needed to check supply vs. expected 
harvest. To overcome these limitations, and speed up the calibration process, we developed an additional 
Harvest Allocation Tool (HAT). Specifically, HAT distributes the amount of harvest formulated separately as 
IRW and FW expected harvest, according to the amount of biomass available in forests for each time step 
during the simulation, taking into account the contribution of salvage logging after natural disturbances, and 
the various management systems defined under different scenarios. Specifically, working with a resolution of 
a time step of one year facilitates an appropriate simulation based on forest conditions during each 
simulation. The silvicultural practices and expected roundwood destinations information are described in 
unique input files, which allow a transparent picture and comparison. 
2.3 EU-CBM-HAT software packages 
The forest carbon accounting team of the Canadian Forest Service reimplemented the core CBM-CFS3 as a 
C++ library with interface methods for the Python and R languages. The libcbm package was conceived as a 
generic flux/pool computation and libcbm is the main application of the tool. Version 1.0.0 of the libcbm 
package was released in early 2022 on github (https://github.com/cat-cfs/libcbm_py). The input data approach 
based on csv input files is consistent with the CBM-CFS3. The archive index database (AIDB) is based on 
SQLite (https://www.sqlite.org/index.html). libcbm_py contains a script to translate the AIDB from the old 
Microsoft Access database format to the new SQLite database format. In the early stages of development, 
the CFS has developed a suite of tests to ensure compatibility between CBM-CFS3 and libcbm where both 
simulations run in parallel, and results are compared at the end. See also an overview of some of our own 
comparison for EU countries in Annex 2.  Adaptation to the EU datasets was done in collaboration between the 
JRC and the CFS. Using this tool will also ensure we stay up to date with any new capabilities CFS adds to 
libcbm. 
On top of libcbm, we created scripts that run our model in a Python package called eu_cbm_hat. HAT and 
COMBO described in the later sections have been implemented as objects inside this package. Python package 
eu_cbm_hat together with rest of simulation infrastructure (e.g. directory and files) required to run a 
simulation represent the EU-CBM-HAT model. 
Although this technical report refers to development designed for the EU block, the tool can be adjusted to 
any individual EU member country or to any other country, or to any other geographical or administrative 
scale. 
Both projects are released under open-source licences: the Canadian package libcbm_py is released by the 
Canadian Forest Service of Natural Resources Canada under the Mozilla public licence. The European package 
is released by the European Commission Joint Research Centre under the MIT and EUPL licence. Installation 
instructions are available on the project gitlab page: https://gitlab.com/bioeconomy/eu_cbm. The maintenance 
and future development of each package falls within the corresponding institutions.

## Стр. 10

7 
3 EU-CBM-HAT architecture: combination of scenarios by “COMBO” 
EU-CBM-HAT basically works as an integration of two EU specific modules developed by the JRC in 
collaboration with the CFS, i.e. the “scenario combination tool”, COMBO, and the “harvest allocation tool”, HAT, 
both integrated with the “libcbm” core, developed by the CFS.   
Hierarchically and functionally, the COMBO is overarching the other two modules. The COMBO tool allows 
combining scenarios including on natural disturbances and human-driven activities under an unlimited number 
of scenarios. Once the combination of scenarios is defined, the HAT estimates the harvest availability and 
allocates the industrial roundwood and fuelwood harvest accordingly.  
Specifically, EU-CBM-HAT can implement both predetermined events on forests and the forestry. 
Predetermined events are assumed as driven by forces outside the forestry sector, such as afforestation, 
deforestation, stand replacing and non-stand replacing natural disturbances. Some of them may result in an 
unplanned roundwood availability through salvage logging, which would be eligible to contribute to meeting 
the expected harvests through specific silvicultural interventions, which in turn can be compensated by 
reduced planned harvest. By opposition, anticipated events are the planned silvicultural interventions, i.e. 
thinnings, final cuts. 
Based on such philosophy, EU-CBM-HAT distinguishes five inputs packages, each one dedicated to a family of 
events with similar general features: conversion to forests (”afforestation”), conversion from forests 
(”deforestation”), stand replacing natural disturbances where events trigger of a new stand cycle ( ”nd_sr”), 
non-stand replacing natural disturbances which affect various pools without starting of a new stand cycle 
(”nd_ns”r), and forest management (”mgmt”) that include regular silvicultural practices applied to the 
concerned forests. The denomination of these packages should be taken in a broad sense, so any type of 
event can potentially fit under one of the packages. As projections may require dynamic changes during the 
simulated period, COMBO allows maximum flexibility regarding silvicultural practices and wood use type, i.e. 
unlimited switch across scenarios during the simulated period. 
In the architecture of the EU-CBM-HAT there are two levels of input-output information: an upper level where 
the user provides the assumptions and data common for all EU member states, and a lower level where 
country specific data, inputs and outputs, are loaded. Each level includes various directories and subdirectories 
which will be described in detail within the following sections. Both input and output data are organized at the 
country level, which also allows running scenarios. 
3.1 Upper level of the EU-CBM-HAT: input information common at EU level 
The upper level of EU-CBM-HAT includes five directories, containing a set of information common for all the 
EU member states, i.e. valid at EU level (Figure 1). This information is used both by HAT, in distributing the 
expected harvest, and by libcbm for the actual simulation. The country directories contain various predefined 
templates (downloadable with the installation, see Annex 1) to be filled in by the user (Table 1). 
Figure 1. Upper architecture of the input data in the EU-CBM-HAT: overview of the mandatory directory and the files in 
the “data” directory.

## Стр. 11

8 
Table 1. Main directories included within EU-CBM-HAT. 
Directory name 
Description of the directory’s content 
countries 
Country specific data as the lower level of the architecture in Figure 2 and details 
are reported in Table 2. 
common 
Info on the applicable forest inventory year in reference_years.csv and international 
codes of the country (e.g. iso2_code) in country_codes.csv.  
combos 
.yaml files which contain explicit information on the combinations of scenarios 
underlying a unique run, e.g. combination of the scenarios for all input data for the 
“reference” scenario in reference .yaml file. 
domestic_harvest 
Contains unlimited number of subdirectories, each subdirectory corresponds to one 
harvest scenario, e.g. subdirectory “reference” for the default dataset.  
Each such subdirectory includes two files with the time series of the expected 
harvest distinguished between industrial roundwood (IRW) and fuelwood (FW), i.e. 
two time series, in irw_harvest.csv, and fw_harvest.csv. The values are defined in 
1000m3 under-bark (according the definitions implemented by the UNECE Joint 
Forest Sector Questionnaire). IRW includes the roundwood which is expected to get a 
commodity use (i.e. no matter if for sawnwood, panels or pulp). FW includes all the 
wood components used for energy. Both are defined as roundwood under-bark.  
Additionally, each subdirectory may contain an additional file rw_harvest.csv 
reporting the expected roundwood harvest which is used for the calibration of the 
model during the historical period (i.e. the period of time between the NFI reference 
year and the beginning of the simulation period), or for post-processing. In fact, the 
roundwood amount is defined as the sum of IRW and FW under-bark. 
output 
Contains unlimited number of subdirectories, one subdirectory for each combination 
of scenarios, e.g. “reference” for the combination of scenarios identified as 
“reference” for all input data. Each subdirectory matches the .yaml file recorded in 
the “combos” directory, with identic names.  
Further down, each subdirectory contains three subdirectories: input, output and 
logs.  
The input directory contains the files fed into libcbm (.csv files assembled by 
COMBO and HAT as a unique set of files requested by the Standard Import Tool 
(SIT)).  
The output directory contains the elaboration of harvest by HAT and the final results 
of the simulation (see also the description of output tables in 3.7 EU-CBM-HAT 
outputs).  
The logs directory contains text files as issued by HAT and libcbm, describing the 
progress of the model running, including various diagnostic messages and detailed 
description of the errors, if any.  
3.2 Lower level of the EU-CBM-HAT: country specific inputs 
The directory “countries” contains one country-directory for each EU member state identified by the iso2_code 
of the country (e.g. BE for Belgium, RO for Romania). Inside each country-directory, all the input files are 
distributed between four directories, as reported on Figure 2 and described in Table 2 .

*Таблица 11.1:*

| Directory name | Description of the directory’s content |
|---|---|
| countries | Country specific data as the lower level of the architecture in Figure 2 and details are reported in Table 2. |
| common | Info on the applicable forest inventory year in reference_years.csv and international codes of the country (e.g. iso2_code) in country_codes.csv. |
| combos | .yaml files which contain explicit information on the combinations of scenarios underlying a unique run, e.g. combination of the scenarios for all input data for the “reference” scenario in reference .yaml file. |
| domestic_harvest | Contains unlimited number of subdirectories, each subdirectory corresponds to one harvest scenario, e.g. subdirectory “reference” for the default dataset. Each such subdirectory includes two files with the time series of the expected harvest distinguished between industrial roundwood (IRW) and fuelwood (FW), i.e. two time series, in irw_harvest.csv, and fw_harvest.csv. The values are defined in 1000m3 under-bark (according the definitions implemented by the UNECE Joint Forest Sector Questionnaire). IRW includes the roundwood which is expected to get a commodity use (i.e. no matter if for sawnwood, panels or pulp). FW includes all the wood components used for energy. Both are defined as roundwood under-bark. Additionally, each subdirectory may contain an additional file rw_harvest.csv reporting the expected roundwood harvest which is used for the calibration of the model during the historical period (i.e. the period of time between the NFI reference year and the beginning of the simulation period), or for post-processing. In fact, the roundwood amount is defined as the sum of IRW and FW under-bark. |
| output | Contains unlimited number of subdirectories, one subdirectory for each combination of scenarios, e.g. “reference” for the combination of scenarios identified as “reference” for all input data. Each subdirectory matches the .yaml file recorded in the “combos” directory, with identic names. Further down, each subdirectory contains three subdirectories: input, output and logs. The input directory contains the files fed into libcbm (.csv files assembled by COMBO and HAT as a unique set of files requested by the Standard Import Tool (SIT)). The output directory contains the elaboration of harvest by HAT and the final results of the simulation (see also the description of output tables in 3.7 EU-CBM-HAT outputs). The logs directory contains text files as issued by HAT and libcbm, describing the progress of the model running, including various diagnostic messages and detailed description of the errors, if any. |

## Стр. 12

9 
Figure 2. Lower architecture of the input data in the EU-CBM-HAT:  overview of the directories and files included within 
each “country” directory (corresponding to box “Directory: countries” in Figure 1). 
 
 
Country specific information is made available to EU-CBM-HAT in four directories as described in Table 2. This 
information is used to distribute the expected harvest and for the preparation of files required by SIT. 
Table 2. Top-down description of the subdirectories included within each country-directory (detailed description in the 
following sections). 
Directory 
Description of content 
common 
Three files (see Table 3) with data applicable to all events. 
silv 
Four files (see Table 3) containing the specifications of the applicable silvicultural 
practices and characteristics of roundwood use. Further down, each file may contain data 
for an unlimited number of scenarios. 
config 
Two files (see Table 3) mapping the AIDB initialization and simulation assumptions. 
activities 
Five directories with data specific to each of the following five packages: afforestation, 
deforestation, stand replacing and non-stand replacing natural disturbances and forest 
management. Further down, each file may contain data for an unlimited number of 
scenarios (see Table 3). 
The subdirectories “common” and “activities” contain specific input files organized according to the 
information and formats required by the libcbm’s SIT. These are consistent with the CBM-CFS3 required inputs 
(Table 3).  
Table 3. Specific input files expected by libcbm’s SIT. 
SIT country specific input (1); file name 
EU-CBM-HAT directory/ies 
Age Classes; age_class.csv 
common 
Classifiers and Values; classifiers.csv 
common

*Таблица 12.1:*

| Directory | Description of content |
|---|---|
| common | Three files (see Table 3) with data applicable to all events. |
| silv | Four files (see Table 3) containing the specifications of the applicable silvicultural practices and characteristics of roundwood use. Further down, each file may contain data for an unlimited number of scenarios. |
| config | Two files (see Table 3) mapping the AIDB initialization and simulation assumptions. |
| activities | Five directories with data specific to each of the following five packages: afforestation, deforestation, stand replacing and non-stand replacing natural disturbances and forest management. Further down, each file may contain data for an unlimited number of scenarios (see Table 3). |

*Таблица 12.2:*

| SIT country specific input (1); file name | EU-CBM-HAT directory/ies |
|---|---|
| Age Classes; age_class.csv | common |
| Classifiers and Values; classifiers.csv | common |

## Стр. 13

10 
Disturbance Types; disturbance_types.csv 
common 
Inventory; inventory_csv 
Growth and Yields; growth_curves.csv 
Disturbance Events; events.csv 
Transition Rules; transitions.csv 
activities/afforestation 
activities/deforestation  
activities/ stand replacing natural disturbances 
activities/non-stand 
replacing 
natural 
disturbances 
activities/forest management 
(1) The content of these files is described in the CBM-CFS3 user’s guide (Kull et al., 2019). 
3.3 Directory “common”: information applicable to all events 
This directory includes three input files (as of Table 3), reporting the data common to all disturbance events 
which may occur in forest; therefore, they are organized as unique input files. 
3.4 Directory “silv”: description of silvicultural practices, factors for roundwood 
destination, for volume to biomass conversion and market modifiers  
The directory contains the information describing the silvicultural operations and the factors quantifying the 
IRW and FW shares in the roundwood removal (Table 4). It also includes the factors for the modulation of 
harvest according to the market demand, as well as the factors for converting volume to carbon content. This 
information is used by HAT to distribute the harvest across available stands and to prepare the disturbance 
events data for the actual simulation. 
Table 4. Input required by the HAT module in distributing the harvest and constructing the “events” inputs. 
File name  
Description of content 
events_template.csv 
Provides the description of each silvicultural practice applicable. Silvicultural 
practices are attached to regular silvicultural interventions in forests, including 
those following specific natural disturbances (i.e. salvage logging in one or 
several steps after the natural disturbance event) and roundwood destination 
(IRW and FW, or FW only). The description includes the combination of classifiers 
specifying where, and within each age interval, a silvicultural operation is 
applicable (see Table 5). 
harvest_factors.csv 
Contains time series with values reporting the market “skew” factor (ϒ). The 
market factor adjusts the allocation of IRW, based on IRW availability and 
market shocks during the simulation (see section 4 Distribute the expected 
harvest: harvest allocation tool (HAT)). This factor can be applied either for each 
silvicultural practice, or, as default option, to species’ grouping (i.e. coniferous 
and broadleaved).  
The default option is that the expected ratio of coniferous and broadleaves wood 
in IRW harvest has to be provided by the user. The values of ϒ need to be 
provided for every year during the simulation. The default value is ϒ = 1 when 
the IRW is allocated strictly according to the biomass availability, according to 
applicable silvicultural practices. This allocation can be modified by the user (e.g. 
to increase/decrease the roundwood harvest from final cut in spruce forest in 
one specific year along the simulated period, see Eq. (9) and Eq. (10) in 4.3 
Distribution of the industrial roundwood and fuelwood harvests). 
By default, the FW is distributed according to the availability, without possibility 
to modify it through a market factor.

*Таблица 13.1:*

| Disturbance Types; disturbance_types.csv | common |
|---|---|
| Inventory; inventory_csv Growth and Yields; growth_curves.csv Disturbance Events; events.csv Transition Rules; transitions.csv | activities/afforestation |
|  | activities/deforestation |
|  | activities/ stand replacing natural disturbances |
|  | activities/non-stand replacing natural disturbances |
|  | activities/forest management |

*Таблица 13.2:*

| File name | Description of content |
|---|---|
| events_template.csv | Provides the description of each silvicultural practice applicable. Silvicultural practices are attached to regular silvicultural interventions in forests, including those following specific natural disturbances (i.e. salvage logging in one or several steps after the natural disturbance event) and roundwood destination (IRW and FW, or FW only). The description includes the combination of classifiers specifying where, and within each age interval, a silvicultural operation is applicable (see Table 5). |
| harvest_factors.csv | Contains time series with values reporting the market “skew” factor (ϒ). The market factor adjusts the allocation of IRW, based on IRW availability and market shocks during the simulation (see section 4 Distribute the expected harvest: harvest allocation tool (HAT)). This factor can be applied either for each silvicultural practice, or, as default option, to species’ grouping (i.e. coniferous and broadleaved). The default option is that the expected ratio of coniferous and broadleaves wood in IRW harvest has to be provided by the user. The values of ϒ need to be provided for every year during the simulation. The default value is ϒ = 1 when the IRW is allocated strictly according to the biomass availability, according to applicable silvicultural practices. This allocation can be modified by the user (e.g. to increase/decrease the roundwood harvest from final cut in spruce forest in one specific year along the simulated period, see Eq. (9) and Eq. (10) in 4.3 Distribution of the industrial roundwood and fuelwood harvests). By default, the FW is distributed according to the availability, without possibility to modify it through a market factor. |

## Стр. 14

11 
irw_fract_by_dist.csv 
Specifies the expected share of IRW in the roundwood removals for each forest 
type by each applicable silvicultural practice (see Table 6). 
vol_to_mass_coeff.csv 
Contains the values of wood density (“wood_density”) and the proportion of bark 
in total standing volume (“bark_frac”) for each forest type. It may also contain 
other input data with the similar aggregation as needed for post-processing (e.g. 
biomass expansion factor values provided on forest types, etc). 
Silvicultural practices resulting in wood removals are listed in the disturbance_types.csv file (included under 
the “common” directory) and described through quantitative characteristics in the events_templates.csv input 
file included within the directory “silv”. Their correspondence to AIDB disturbances is specified in 
associations.csv. This last file includes all eligibility criteria linked to the specific silvicultural practices (Table 
5). HAT uses this information to distribute the harvest across eligible stands and pools, and builds the events 
input into libcbm module.  
Table 5. Description of the silvicultural practices as required by HAT in events_templates.csv. This table contains only the 
elements which are specific to EU-CBM-HAT, in addition to typical descriptors for “events” input required by libcbm, 
described in CBM-CFS3 User’s Guide (Kull et al., 2019).  
Descriptor 
Description  
scenario 
Identifier for the package of input data specific to each assumption, i.e. it 
allows differentiating between assumptions. Among others, it represents the 
key in defining combination of scenarios in .yaml file. 
growth_period 
“Cur” stands for input data reflecting the current increment tables, which are 
applied during the simulation, as opposed to “Init”, which represents yield 
tables used during the initialization period of the simulation (see Pilli et al., 
2013, Figure 3), e.g. standing stocks expected at various ages. The 
corresponding data is provided in the growth_curves.csv input file. By default, 
“Cur” is used. 
product_created 
The silvicultural practices labelled as “IRW_and_FW” are expected to provide 
both IRW and FW (i.e. their share in the roundwood harvested is available in 
the file irw_frac_by_dist.csv). Silvicultural practices associated with “FW_only” 
do provide FW only.  
dist_type_name 
Denomination of the applicable silvicultural practice, e.g. thinning, with 
average of 22% intensity per standing volume, etc. This has to correspond to 
value used for “dist_desc_input” from disturbance_type.csv file and 
“name_input” in the associations.csv.  
min_since_last_dist 
Used by HAT and later libcbm to filter eligible disturbances according to a 
minimum return time between two consecutive disturbances (see also 
“dist_interval_bias”). The default value is set to -1, i.e. the return time is not 
relevant. 
max_since_last_dist 
The value is always set to -1, i.e. the information is not relevant for HAT. 
dist_interval_bias 
A value representing the expected period of time (in years) for which the total 
amount of IRW available through a specific silvicultural practice can be 
assumed as being entirely removed from forest, in equal shares annually 
between the two age limits. It is equivalent to the expected disturbance return 
in the same stand. HAT uses it to annualize the total available amount, 
resulting in the amount available for each silvicultural intervention in a time 
step. In general, it is equal to “min_since_last_dist” for non-stand replacing 
silvicultural interventions. For stand-replacing ones, it is equal to the duration 
corresponding to the period when termination of all stands in the oldest age

*Таблица 14.1:*

| irw_fract_by_dist.csv | Specifies the expected share of IRW in the roundwood removals for each forest type by each applicable silvicultural practice (see Table 6). |
|---|---|
| vol_to_mass_coeff.csv | Contains the values of wood density (“wood_density”) and the proportion of bark in total standing volume (“bark_frac”) for each forest type. It may also contain other input data with the similar aggregation as needed for post-processing (e.g. biomass expansion factor values provided on forest types, etc). |

*Таблица 14.2:*

| Descriptor | Description |
|---|---|
| scenario | Identifier for the package of input data specific to each assumption, i.e. it allows differentiating between assumptions. Among others, it represents the key in defining combination of scenarios in .yaml file. |
| growth_period | “Cur” stands for input data reflecting the current increment tables, which are applied during the simulation, as opposed to “Init”, which represents yield tables used during the initialization period of the simulation (see Pilli et al., 2013, Figure 3), e.g. standing stocks expected at various ages. The corresponding data is provided in the growth_curves.csv input file. By default, “Cur” is used. |
| product_created | The silvicultural practices labelled as “IRW_and_FW” are expected to provide both IRW and FW (i.e. their share in the roundwood harvested is available in the file irw_frac_by_dist.csv). Silvicultural practices associated with “FW_only” do provide FW only. |
| dist_type_name | Denomination of the applicable silvicultural practice, e.g. thinning, with average of 22% intensity per standing volume, etc. This has to correspond to value used for “dist_desc_input” from disturbance_type.csv file and “name_input” in the associations.csv. |
| min_since_last_dist | Used by HAT and later libcbm to filter eligible disturbances according to a minimum return time between two consecutive disturbances (see also “dist_interval_bias”). The default value is set to -1, i.e. the return time is not relevant. |
| max_since_last_dist | The value is always set to -1, i.e. the information is not relevant for HAT. |
| dist_interval_bias | A value representing the expected period of time (in years) for which the total amount of IRW available through a specific silvicultural practice can be assumed as being entirely removed from forest, in equal shares annually between the two age limits. It is equivalent to the expected disturbance return in the same stand. HAT uses it to annualize the total available amount, resulting in the amount available for each silvicultural intervention in a time step. In general, it is equal to “min_since_last_dist” for non-stand replacing silvicultural interventions. For stand-replacing ones, it is equal to the duration corresponding to the period when termination of all stands in the oldest age |

## Стр. 15

12 
class is expected, i.e. 20-40 years for shelter-wood systems, or a period equal 
to the difference of max and min ages for the applicable silvicultural practice. 
Its value drives the length of the cycles for even-aged stands, as well as the 
contribution of final cuts to total harvest in a time step.   
last_dist_id 
Define a successive mandatory silvicultural practice for a prior silvicultural 
practice (i.e. 2nd cut or final cut in stand replacing by multiple interventions) 
or following a natural disturbance (i.e. salvage logging). 
sw_start/hw_start 
& 
sw_end /hw_end 
Values representing the start and the end of the stands’ age range when a 
specific silvicultural practice applies. For successive silvicultural practices, 
these ranges cannot overlap, while they allow gaps, i.e. as to define an age 
interval when no silvicultural interventions apply.  
Note that the silvicultural practices can be changed during the simulation shifting from one scenario (e.g. 
reference) to another (e.g. close-to-nature) in any time step during the simulation period. The shift has to be 
defined in .yaml before the simulation start (see 3.9 Creating a new combination of scenarios). 
The details regarding the expected roundwood destinations, as IRW or FW are reported in 
irw_fract_by_dist.csv (Table 6). HAT considers the IRW as a generic roundwood category which includes all 
sorts of roundwood that are expected to have a material use from the following pools: merchantable living 
biomass, other wood components (including branches and tops, or parts of them), stem snags and branch 
snags. This file specifies, for all applicable silvicultural practices, the fraction of total roundwood material 
potentially used as IRW. The remaining fraction is assumed by default as FW, as a collateral product, e.g. if 
the IRW fraction is equal to 10%, 90% of roundwood removal would be classified as collateral fuelwood.  
Table 6. Assumptions and default values regarding the fractions of industrial roundwood in the roundwood removals 
from forests (irw_fract_by_dist.csv). 
Descriptor 
Description 
scenario 
Name of the applicable scenario within a run; a change to 
another scenario can occur at any moment in time during 
the simulation. 
softwood_merch 
softwood_other 
softwood_stem_snag 
softwood_branch_snag 
hardwood_merch 
hardwood_other 
hardwood_stem_snag 
hardwood_branch_snag 
Fraction of roundwood material available as IRW from a 
specified pool by a specific silvicultural practice for each 
forest type. Fractions have to be generated based on under-
bark volume. 
The roundwood amount removed from a specified forest 
pool is the product between the standing stock, multiplied by 
the fraction affected by the silvicultural practice (e.g. 20% of 
standing biomass and 80% of standing dead wood for 
commercial thinning), finally split between IRW and FW 
based on the IRW fraction reported in this cell (e.g. 20%) 
(see 4.3 Distribution of the industrial roundwood and 
fuelwood harvests).  
The definitions of the four source pools are consistent with 
the general description reported on the CBM-CFS3 User’s 
Guide. 
Default values for IRW fraction1,2 
softwood_merch 
< 10% for early thinning  
30-50% for mid-late thinning  
90% for late thinning and final cut

*Таблица 15.1:*

|  | class is expected, i.e. 20-40 years for shelter-wood systems, or a period equal to the difference of max and min ages for the applicable silvicultural practice. Its value drives the length of the cycles for even-aged stands, as well as the contribution of final cuts to total harvest in a time step. |
|---|---|
| last_dist_id | Define a successive mandatory silvicultural practice for a prior silvicultural practice (i.e. 2nd cut or final cut in stand replacing by multiple interventions) or following a natural disturbance (i.e. salvage logging). |
| sw_start/hw_start & sw_end /hw_end | Values representing the start and the end of the stands’ age range when a specific silvicultural practice applies. For successive silvicultural practices, these ranges cannot overlap, while they allow gaps, i.e. as to define an age interval when no silvicultural interventions apply. |

*Таблица 15.2:*

| Descriptor | Description |
|---|---|
| scenario | Name of the applicable scenario within a run; a change to another scenario can occur at any moment in time during the simulation. |
| softwood_merch softwood_other softwood_stem_snag softwood_branch_snag hardwood_merch hardwood_other hardwood_stem_snag hardwood_branch_snag | Fraction of roundwood material available as IRW from a specified pool by a specific silvicultural practice for each forest type. Fractions have to be generated based on under- bark volume. The roundwood amount removed from a specified forest pool is the product between the standing stock, multiplied by the fraction affected by the silvicultural practice (e.g. 20% of standing biomass and 80% of standing dead wood for commercial thinning), finally split between IRW and FW based on the IRW fraction reported in this cell (e.g. 20%) (see 4.3 Distribution of the industrial roundwood and fuelwood harvests). The definitions of the four source pools are consistent with the general description reported on the CBM-CFS3 User’s Guide. |
| Default values for IRW fraction1,2 |  |
| softwood_merch | < 10% for early thinning 30-50% for mid-late thinning 90% for late thinning and final cut |

## Стр. 16

13 
50% in case of deforestation 
softwood_other 
0% 
softwood_stem_snag 
10% for sanitary cuttings  
80% for salvage logging in the first year of the disturbance  
30% in the second year of the disturbance  
0% for the salvage logging in the following years 
50% in case of deforestation 
softwood_branch_snag 
0% 
hardwood_merch 
10% for early thinning  
20-30% for late thinnings  
75% for late thinning and final cuts 
50% in case of deforestation 
hardwood_other 
0% 
hardwood_stem_snag 
20% for sanitary cuttings  
80% for salvage logging in the first year of the disturbance  
40% in the second year of the disturbance  
0% for the salvage logging in the following years 
50% in case of deforestation 
hardwood_branch_snag 
0% 
(1) assuming some of these sources can provide wood for commodity use. 
(2) based on literature, validated runs of CBM-CFS3 and general knowledge (e.g. Luke, 2021; Ruter, 20219; Skogsstyrelsen, 2022; ). 
Note that the fraction of IRW can be changed for any time step during a simulation, i.e. shifting from one 
scenario to another (e.g. reference scenario to high-harvesting-protocol). Moreover, the shift to a new wood 
use scenario can be done independently by the shift to a new scenario regarding the silvicultural practices, e.g. 
they can occur at different moments during the simulation. The shifts have to be defined in .yaml file before 
the simulation start. 
Finally, wood density and bark fractions are used by HAT to convert back and forth from carbon to volume, in 
order to allocate the harvest according to the availability in the standing stocks (Table 7). The values are 
provided for forest types only. See section 4.4 Uncertainty and inconsistency in distributing the harvests for 
the discussion on how these factors can influence the emissions and removals projections of EU-CBM-HAT. 
Table 7. Input data for conversion of volume to biomass and bark fraction in standing volume in vol_to_mass_coefs.csv.  
Descriptor 
Description 
wood_density 
Wood density coefficient, i.e. a constant non-age dependent value, reported 
in t dry matter per 1 m3 and derived from a literature review. Generally, it 
is a country specific average value, as reported, for example, in the 
country’s National Inventory Report to GHG inventory submitted by the 
country to UNFCCC. It needs to be consistent with Boudewyn eqs. selected 
for the conversion of volume to biomass.  
bark_frac 
Bark’s fraction of the merchantable volume, i.e. a constant non-age 
dependent parameter, as a percentage in the standing volume (%).

*Таблица 16.1:*

|  | 50% in case of deforestation |
|---|---|
| softwood_other | 0% |
| softwood_stem_snag | 10% for sanitary cuttings 80% for salvage logging in the first year of the disturbance 30% in the second year of the disturbance 0% for the salvage logging in the following years 50% in case of deforestation |
| softwood_branch_snag | 0% |
| hardwood_merch | 10% for early thinning 20-30% for late thinnings 75% for late thinning and final cuts 50% in case of deforestation |
| hardwood_other | 0% |
| hardwood_stem_snag | 20% for sanitary cuttings 80% for salvage logging in the first year of the disturbance 40% in the second year of the disturbance 0% for the salvage logging in the following years 50% in case of deforestation |
| hardwood_branch_snag | 0% |

*Таблица 16.2:*

| Descriptor | Description |
|---|---|
| wood_density | Wood density coefficient, i.e. a constant non-age dependent value, reported in t dry matter per 1 m3 and derived from a literature review. Generally, it is a country specific average value, as reported, for example, in the country’s National Inventory Report to GHG inventory submitted by the country to UNFCCC. It needs to be consistent with Boudewyn eqs. selected for the conversion of volume to biomass. |
| bark_frac | Bark’s fraction of the merchantable volume, i.e. a constant non-age dependent parameter, as a percentage in the standing volume (%). |

## Стр. 17

14 
3.5 Directory “config”: mapping simulation assumptions to generalized 
assumptions 
The directory contains country specific information allowing SIT to map the specific assumptions of each 
simulation to the parameters stored in the AIDB (Table 8) as generalized assumptions. EU CBM-HAT uses the 
customized archive index database for European Union countries (Pilli et al., 2018), which was improved along 
the EU-CBM-HAT development with additional explicit fluxes, i.e. from merchantable, other wood components, 
stem and branch snag pools, to product pool. 
Table 8. Files placed within the “config” directory. 
Input file name  
Description of the information contained 
AIDB 
Country specific archive index database. 
associations.csv 
File displaying complete list for mapping the codes from input data to 
corresponding categories from AIDB, e.g. classifiers to classifiers, disturbance 
types to disturbances types, etc. 
The association.csv file includes the mapping rules for running the simulation (Table 9) for all activities, e.g. 
each classifier and disturbance need to be mapped to a corresponding item in the AIDB. Missing elements 
trigger a message at the begging of the simulated period (after the calibration, see 6 Automatic checks of the 
input data and error messages during the runs).  
Table 9. Example of mapping of the input data with AIDB categories in associations.csv. The “name_input” is the name 
used for that respective category across the input data files, while the “name_aidb” is the name for the corresponding 
item in the AIDB. 
Category 
name_input 
name_aidb 
MapAdminBoundary 
Luxembourg 
Luxembourg 
MapEcoBoundary 
CLU24 
CLU24 
MapSpecies 
..... 
..... 
MapDisturbanceType 
Generic 5% 
generic 5% mortality 
MapSpecies 
non-forest to species or forest types 
Average 
3.6 Directory “activities”: input data describing disturbance events 
The disturbance events assumptions are included within the directory “activities” and defined in five different 
subdirectories: afforestation, deforestation, stand replacing and non-stand replacing natural disturbances, and 
forest management. While each subdirectory contains four files necessary to describe relevant inputs for that 
family of events, only files from the subdirectory forest management are mandatory with data (Table 10). 
This means that for other family of events empty tables are accepted, e.g. assuming there is no scenario for a 
specific type of disturbance, or there is no specific assumption regarding the inventory, growth curves or 
transitions relevant for that disturbance. In such cases, the information provided for forest management is 
implicitly used (as submitted in subdirectory “mgmt”). By default, the installation of EU-CBM-HAT provides for 
the full set of required files. 
Table 10. Generic description of the content of the mandatory input for disturbance events. 
Required files 
Description of the content 
events.csv 
Time series including the expected intensity of each disturbance 
event 
(natural 
disturbance, 
silvicultural 
practice), 
further

*Таблица 17.1:*

| Input file name | Description of the information contained |
|---|---|
| AIDB | Country specific archive index database. |
| associations.csv | File displaying complete list for mapping the codes from input data to corresponding categories from AIDB, e.g. classifiers to classifiers, disturbance types to disturbances types, etc. |

*Таблица 17.2:*

| Category | name_input | name_aidb |
|---|---|---|
| MapAdminBoundary | Luxembourg | Luxembourg |
| MapEcoBoundary | CLU24 | CLU24 |
| MapSpecies | ..... | ..... |
| MapDisturbanceType | Generic 5% | generic 5% mortality |
| MapSpecies | non-forest to species or forest types | Average |

*Таблица 17.3:*

| Required files | Description of the content |
|---|---|
| events.csv | Time series including the expected intensity of each disturbance event (natural disturbance, silvicultural practice), further |

## Стр. 18

15 
distinguished by classifiers, and defined as area affected from a 
disturbance event, or as amount of C removed (i.e. for thinnings), or 
proportion of eligible stands affected from a specific event. 
growth_curves.csv 
Two data series with growth curves reporting the standing stock 
volume in m3 per ha on the applicable age classes for each 
combination of classifiers.  
One data series represents the “Init” including the yield curves 
derived from the NFI standing stock volume along the applicable 
age classes. These curves are used for the initialization of the 
carbon stocks in soil, litter and dead wood pools, and to determine 
the carbon stock in living biomass at the beginning of the 
simulation period (i.e. time step 0). See Pilli et al., 2013 Figure 3 for 
an illustration. The second data series labelled as ”Cur” represents 
the expected cumulated net increment of the standing stock 
volume along the applicable age classes (e.g. as retrieved from 
NFI). This curve is used to simulate the biomass growth during the 
simulation. Across the input tables the information on which yield 
curve is required is defined in the column “growth_period”. 
Alternative growth and yield scenarios can be defined, e.g. under 
modified environmental conditions. 
inventory.csv 
Forest inventory data in the initial year of the simulation, 
distinguished between classifiers, with the area distributed on age-
classes or age simply. It should also contain the non-forest area 
expected to be afforested during the entire simulation period.   
transitions.csv 
Transition rules defining changes following specific disturbance 
events (i.e. in case of afforestation or deforestation, or stand 
replacing disturbance events), e.g. from one forest type to another. 
In all these files, wildcards can be used instead of explicit classifiers.  
Before the model run, HAT merges all these inputs into unique set of files in SIT required format (as defined in 
Table 3), and pushes them to libcbm for the actual simulation of the time step. 
3.6.1 Defining simulations regarding the conversion to forests 
The inputs related to the conversion to forests are provided in the subdirectory “afforestation” (Table 11), 
including a time series of the area afforested for the entire projected period. Each of these files contain 
packages of input data on the applicable scenarios (e.g. scenario “3 billion trees pledge”, scenario “natural 
expansion”, etc). 
Table 11. Specific input data required for the conversion to forest. 
Required files 
Description of the content 
inventory.csv 
Total area (in ha) available to be converted to forests during the 
entire simulation period. All classifiers have to be defined.  
growth_curves.csv 
Increment curves (in m3 per ha on age class) for each combination 
of classifiers. These curves will only include the current increment 
curves (i.e. ”Cur”) since they are not subject to initialization period 
and also assumes that there are no silvicultural intervention during 
a transition period from non-forest to forest. Optionally, these 
curves can be afforestation specific (e.g. applying for the transition 
period from non-forest to forest), but a transition to general curves 
should be applied sometime later in order to ensure consistency 
within typical forests in the country. These forests become subject

*Таблица 18.1:*

|  | distinguished by classifiers, and defined as area affected from a disturbance event, or as amount of C removed (i.e. for thinnings), or proportion of eligible stands affected from a specific event. |
|---|---|
| growth_curves.csv | Two data series with growth curves reporting the standing stock volume in m3 per ha on the applicable age classes for each combination of classifiers. One data series represents the “Init” including the yield curves derived from the NFI standing stock volume along the applicable age classes. These curves are used for the initialization of the carbon stocks in soil, litter and dead wood pools, and to determine the carbon stock in living biomass at the beginning of the simulation period (i.e. time step 0). See Pilli et al., 2013 Figure 3 for an illustration. The second data series labelled as ”Cur” represents the expected cumulated net increment of the standing stock volume along the applicable age classes (e.g. as retrieved from NFI). This curve is used to simulate the biomass growth during the simulation. Across the input tables the information on which yield curve is required is defined in the column “growth_period”. Alternative growth and yield scenarios can be defined, e.g. under modified environmental conditions. |
| inventory.csv | Forest inventory data in the initial year of the simulation, distinguished between classifiers, with the area distributed on age- classes or age simply. It should also contain the non-forest area expected to be afforested during the entire simulation period. |
| transitions.csv | Transition rules defining changes following specific disturbance events (i.e. in case of afforestation or deforestation, or stand replacing disturbance events), e.g. from one forest type to another. |

*Таблица 18.2:*

| Required files | Description of the content |
|---|---|
| inventory.csv | Total area (in ha) available to be converted to forests during the entire simulation period. All classifiers have to be defined. |
| growth_curves.csv | Increment curves (in m3 per ha on age class) for each combination of classifiers. These curves will only include the current increment curves (i.e. ”Cur”) since they are not subject to initialization period and also assumes that there are no silvicultural intervention during a transition period from non-forest to forest. Optionally, these curves can be afforestation specific (e.g. applying for the transition period from non-forest to forest), but a transition to general curves should be applied sometime later in order to ensure consistency within typical forests in the country. These forests become subject |

## Стр. 19

16 
to forest management, so contribute to satisfy the expected 
harvest, at any point in time as defined in events_template.csv. 
events.csv 
Area to be afforested for each year during the simulation (in ha 
per year). It has to be split on forest types, while the other 
classifiers can be defined by wildcards. 
transitions.csv  
Transition rules associated with the conversion from non-forest to 
forest land, e.g. continue labelling conversions throughout the 
entire simulation period. Filling in adequately this file, i.e. using a 
peculiar classifier for such events, would allow the user to track 
afforestation related emissions and removals during the entire 
simulated period.  
associations.csv 
Mapping to non-forest soils in AIDB corresponding to non-forest 
land before afforestation. 
3.6.2 Defining simulations regarding the conversions from forests 
The inputs related to conversions from forest to other land categories are provided in the subdirectory 
“deforestation” (Table 12). The roundwood removals associated with the conversion from forest is classified 
as salvage logging from predetermined events and contributes with priority to satisfying the annual expected 
harvest (with shares between IRW and FW as defined in irw_fract_by_dist.csv). Each of these files contain all 
info required for the applicable scenarios (e.g. “historical rate of deforestation”, “minimum historical rate”, etc). 
Table 12. Specific input data required for the conversion from forests. 
Required files 
Description of the content 
events.csv 
Time series with total area (in ha) or total volume (in tC) to be 
converted from forests during the entire simulation period. 
Generally, a random allocation across all classifiers applies. 
transitions.csv  
Defining transitions would allow tracking such conversions 
throughout the simulation period, e.g. in terms of land uses to 
which conversion takes place. Filling in adequately this file, i.e. 
using a peculiar classifier for such events, may allow the user to 
track deforestation area during the entire simulated period. 
irw_fract_by_dist.csv 
Defines the share of IRW for the harvested roundwood. A default 
value of 50% applies, given fact that it may affect stands at any 
age.  
3.6.3 Defining simulations regarding the natural disturbances 
All inputs related to natural disturbances are organized on two types of data reported on the following 
subdirectory: stand replacing (“nd_sr”) and non-stand replacing natural disturbance events (“nd_nsr”) as of 
Table 13. Information on the occurrence and magnitude of natural disturbances is exogenous, defined as time 
series for the entire projected period. As such, EU-CBM-HAT does not predict future disturbances scenarios, 
but demonstrate its ability to accommodate the impacts of such future disturbance events as defined by the 
user. Each of these files contains packages of input data on the applicable scenarios (e.g. “disturbances at 
historical level”, “insect attacks only”, etc). Salvage logging following natural disturbances are considered as 
predetermined events.

*Таблица 19.1:*

|  | to forest management, so contribute to satisfy the expected harvest, at any point in time as defined in events_template.csv. |
|---|---|
| events.csv | Area to be afforested for each year during the simulation (in ha per year). It has to be split on forest types, while the other classifiers can be defined by wildcards. |
| transitions.csv | Transition rules associated with the conversion from non-forest to forest land, e.g. continue labelling conversions throughout the entire simulation period. Filling in adequately this file, i.e. using a peculiar classifier for such events, would allow the user to track afforestation related emissions and removals during the entire simulated period. |
| associations.csv | Mapping to non-forest soils in AIDB corresponding to non-forest land before afforestation. |

*Таблица 19.2:*

| Required files | Description of the content |
|---|---|
| events.csv | Time series with total area (in ha) or total volume (in tC) to be converted from forests during the entire simulation period. Generally, a random allocation across all classifiers applies. |
| transitions.csv | Defining transitions would allow tracking such conversions throughout the simulation period, e.g. in terms of land uses to which conversion takes place. Filling in adequately this file, i.e. using a peculiar classifier for such events, may allow the user to track deforestation area during the entire simulated period. |
| irw_fract_by_dist.csv | Defines the share of IRW for the harvested roundwood. A default value of 50% applies, given fact that it may affect stands at any age. |

## Стр. 20

17 
Table 13. Specific input data required for the natural disturbances. 
Required files 
Description of the content 
events.csv 
Time series with the intensity of each natural disturbance, defined 
as amounts based on volume (converted to tC removed from 
forests), area (in ha) or proportions (% of area) in a wide format 
table with annual time step until the end of the simulation (cells 
can be empty for any time step). 
growth_curves.csv 
Optionally, a different “Cur” curve can be applied after the natural 
disturbances, modifying the growth as a post-event change. 
transitions.csv 
Any specific transition rules linked to such disturbance events, e.g. 
to a new forest type.  
3.6.4 Defining simulations regarding forest management 
All inputs related to forest management activities are contained in the subdirectory “mgmt”.  
Any model run by EU-CBM-HAT, normally, includes two periods.  
The so-called historical period, is used for model’s calibration (i.e. comparing, before 2020 the model output 
with other independent data sources). For this period, the input data reported on the events.csv has to be 
complete, as SIT requires, in explicitly defining the characteristics of the silvicultural practices applied, i.e. 
intensity and frequency of the silvicultural practices, the corresponding amount of harvest, according to the 
recorded statistics (e.g. FAOSTAT, NFI, national statistics), practically the data organized as of old CBM-CFS3 
inputs. Optionally, in order to ensure a realistic age class representation at the end of calibration period, they 
should explicitly include the area affected by stand-replacing disturbance events (i.e. clear-cuts) and/or the 
contribution of salvage logging to harvest. Four specific files are required to simulate the forest management 
during the calibration period (Table 14).  
Table 14. Specific input data required for forest management, for both calibration and simulation period. 
Required files 
Description 
inventory.csv 
Forest inventory data in the initial year of the simulation. Information is 
organized on classifiers with area distributed on age-class. 
growth_curves.csv 
Contains the yield (“Init”) and increment (“Cur”) curves for the relevant 
combination of classifiers. These would be used both for calibration and 
simulation period. 
events.csv 
Time series with data for the historical period used for calibration, i.e. from the 
last before the last inventory year to 2020 (or another). For the period after the 
last year of the calibration period, e.g. post-2020, the table remains empty, as 
all required information would be calculated by HAT and make it available for 
inspections and post-checks in the directory output/...../output/events.csv. 
transitions.csv  
Implement changes caused by disturbances, e.g. to a new forest type, expected 
during both the calibration and simulation period as called by the applicable 
scenario.  
Within the subsequent period, i.e. the so-called simulated period (e.g. from 2021 onward), COMBO and HAT 
bring together the inputs from all types of disturbance events to be simulated during the simulated period in a 
unique forest management boundary where country specific silvicultural interventions are applied. This means 
that all pre-determined disturbances will contribute to shaping the forest dynamics and satisfying the 
harvests, for example, and land afforested earlier becomes subject to silvicultural practices, as well as a 
forest affected by a natural disturbance may be subject to salvage logging. For the simulated period, while

*Таблица 20.1:*

| Required files | Description of the content |
|---|---|
| events.csv | Time series with the intensity of each natural disturbance, defined as amounts based on volume (converted to tC removed from forests), area (in ha) or proportions (% of area) in a wide format table with annual time step until the end of the simulation (cells can be empty for any time step). |
| growth_curves.csv | Optionally, a different “Cur” curve can be applied after the natural disturbances, modifying the growth as a post-event change. |
| transitions.csv | Any specific transition rules linked to such disturbance events, e.g. to a new forest type. |

*Таблица 20.2:*

| Required files | Description |
|---|---|
| inventory.csv | Forest inventory data in the initial year of the simulation. Information is organized on classifiers with area distributed on age-class. |
| growth_curves.csv | Contains the yield (“Init”) and increment (“Cur”) curves for the relevant combination of classifiers. These would be used both for calibration and simulation period. |
| events.csv | Time series with data for the historical period used for calibration, i.e. from the last before the last inventory year to 2020 (or another). For the period after the last year of the calibration period, e.g. post-2020, the table remains empty, as all required information would be calculated by HAT and make it available for inspections and post-checks in the directory output/...../output/events.csv. |
| transitions.csv | Implement changes caused by disturbances, e.g. to a new forest type, expected during both the calibration and simulation period as called by the applicable scenario. |

## Стр. 21

18 
COMBO constructs the overall scenario to be run from the different scenarios on activities (e.g. “business-as-
usual” for afforestation, “close to nature” for forest management, etc), HAT distributes the IRW and FW to 
disturbance events based on the input information in the corresponding files (e.g. events_template.csv, 
irw_frac_by_dist.csv, irw_harvest.csv and fw_harvest.csv) in the SIT required format. The complete files 
generated this way can be visualised at the end of the simulation in the output directory (see 3.7 EU-CBM-
HAT outputs). 
3.7 EU-CBM-HAT outputs 
The directory “output” contains two subdirectories (as of Table 1 and Figure 1) with the HAT prepared “input” 
and the actual “output” of the simulations.  
The directory “input” contains inputs prepared by HAT as .csv files in SIT required format (as of Table 3). These 
files represent a compilation of user’s input data for the calibration period and only the predetermined events 
(natural disturbances, deforestation) and afforestation for the simulated period. 
The subdirectory “output” contains the results of the simulations for both the calibration and simulated 
periods (Table 15), a complete set of inputs either from user and HAT. Results data are available at the most 
detailed scale simulated, by all combination of classifiers and time step of one-year. In order to get a 
complete picture of the calibration and simulation these files need to be explored.  
Table 15. Output files of EU-CBM-HAT.  
Output files 
Description 
area.csv 
Dynamic of area. 
classifiers.csv 
Classifiers according to input data 
events.csv 
Contains HAT prepared target amounts for the silvicultural practices assumed to occur as 
of silvicultural practices described in events_templates.csv. It does not include the target 
amounts for salvage logging (see step 1 in 4.1 HAT concept ) for which the information is 
available in the corresponding input files. In the events.csv the measurement type may be 
changed compared to actual input, given HAT processing all inputs in terms of mass (M). 
extras.csv 
Overview table prepared by HAT providing estimates for generic indicators at the time step 
resolution, i.e. quantities are the totals for the time step. The indicators refer to total annual 
amounts of IRW and FW expected from salvage logging. This file can be used as a first step 
in checking the result of the simulation.    
flux.csv 
Dynamic of the amounts of carbon transferred between various pools.  
pools.csv 
C stocks dynamics for all pools. 
state.csv 
Age and age class dynamic. 
params.csv 
Spatial and temporal tracking of disturbance events 
Output files are saved in a country directory identified by country’s iso code, e.g. there is no EU aggregation 
predefined in EU-CBM-HAT (see 3.8 Exploration of EU-CBM-HAT results for more details).  
The extras.csv and events.csv files are specific outputs provided from EU-CBM-HAT, (see Table 12 and Table 
13). The purpose of these additional files is to increase the transparency on the internal processing applied 
from HAT and to allow quick checks of the simulations.  
Specifically, extras.csv presents the results aggregated by the time steps for the simulated period (Table 16).

*Таблица 21.1:*

| Output files | Description |
|---|---|
| area.csv | Dynamic of area. |
| classifiers.csv | Classifiers according to input data |
| events.csv | Contains HAT prepared target amounts for the silvicultural practices assumed to occur as of silvicultural practices described in events_templates.csv. It does not include the target amounts for salvage logging (see step 1 in 4.1 HAT concept ) for which the information is available in the corresponding input files. In the events.csv the measurement type may be changed compared to actual input, given HAT processing all inputs in terms of mass (M). |
| extras.csv | Overview table prepared by HAT providing estimates for generic indicators at the time step resolution, i.e. quantities are the totals for the time step. The indicators refer to total annual amounts of IRW and FW expected from salvage logging. This file can be used as a first step in checking the result of the simulation. |
| flux.csv | Dynamic of the amounts of carbon transferred between various pools. |
| pools.csv | C stocks dynamics for all pools. |
| state.csv | Age and age class dynamic. |
| params.csv | Spatial and temporal tracking of disturbance events |

## Стр. 22

19 
Table 16. Definitions of the aggregated indicators as reported in extras.csv.  All values in this file are volume under-bark 
(m3) for the annual time step virtualized by HAT for the simulated period (calibration period excluded). 
Indicator 
Description of the indicator 
Quantitative relation to other 
indicators 
Fluxes to products from salvage logging 
irw_predetermined  
fw_predetermined 
Target volume to be generated only 
from salvage logging (i.e. natural 
disturbances and deforestation) or 
from 
predetermined 
silvicultural 
practices (i.e. clear cut areas defined 
for the simulated period). It should be 
noted that only salvage in the year 
when natural disturbance occurs is 
included (i.e. if there is any salvage 
logging in the years following the 
natural disturbance, the corresponding 
contribution to satisfying expected 
harvest is taken into account by HAT, 
see 4.2 Treatment of salvage logging, 
or 
irw_salv_avail 
& 
fw_salv_avail 
below).  
 
Expected harvests formulated by exogenous models (e.g. economic models) 
harvest_irw_vol 
harvest_fw_vol 
Expected harvest of IRW and FW. 
Original values according to the files 
from directory “domestic_harvest”. 
Remaining unsatisfied amounts after any supply from salvage loggings 
irw_salv_avail 
fw_salv_avail 
Target volume to be further satisfied 
from salvage logging in the year(s) 
following the natural disturbances, i.e. 
such volume is harvested with priority 
in the time step before distributing the 
remaining amount. Noteworthy, any 
amount available from salvage logging 
in the following years is accounted by 
HAT with higher priority in distributing 
the 
expected 
harvest 
for 
the 
predefined number of time steps (i.e. if 
salvage is planned to occur in the two 
years following the event, silvicultural 
practices 
associated 
with 
salvage 
logging need to be specified in 
events_template.csv). For example, in 
order to harvest in two years, salvage 
can be set to 60% in the first year and 
100% in the second year). 
100% 
of 
the 
amount 
of 
irw_salv_avail is allocated by HAT in 
the time step. 
100% 
of 
the 
amount 
of 
fw_salv_avail is allocated by HAT in 
the time step. 
remain_irw_harvest 
remain_fw_harvest 
Target volume to be further satisfied 
after any supply from predetermined 
disturbances. 
remain_irw_harvest= 
harvest_irw_vol- irw_predetermined 
remain_fw_harvest= 
harvest_fw_vol-fw_predetermined

*Таблица 22.1:*

| Indicator | Description of the indicator | Quantitative relation to other indicators |
|---|---|---|
| Fluxes to products from salvage logging |  |  |
| irw_predetermined fw_predetermined | Target volume to be generated only from salvage logging (i.e. natural disturbances and deforestation) or from predetermined silvicultural practices (i.e. clear cut areas defined for the simulated period). It should be noted that only salvage in the year when natural disturbance occurs is included (i.e. if there is any salvage logging in the years following the natural disturbance, the corresponding contribution to satisfying expected harvest is taken into account by HAT, see 4.2 Treatment of salvage logging, or irw_salv_avail & fw_salv_avail below). |  |
| Expected harvests formulated by exogenous models (e.g. economic models) |  |  |
| harvest_irw_vol harvest_fw_vol | Expected harvest of IRW and FW. | Original values according to the files from directory “domestic_harvest”. |
| Remaining unsatisfied amounts after any supply from salvage loggings |  |  |
| irw_salv_avail fw_salv_avail | Target volume to be further satisfied from salvage logging in the year(s) following the natural disturbances, i.e. such volume is harvested with priority in the time step before distributing the remaining amount. Noteworthy, any amount available from salvage logging in the following years is accounted by HAT with higher priority in distributing the expected harvest for the predefined number of time steps (i.e. if salvage is planned to occur in the two years following the event, silvicultural practices associated with salvage logging need to be specified in events_template.csv). For example, in order to harvest in two years, salvage can be set to 60% in the first year and 100% in the second year). | 100% of the amount of irw_salv_avail is allocated by HAT in the time step. 100% of the amount of fw_salv_avail is allocated by HAT in the time step. |
| remain_irw_harvest remain_fw_harvest | Target volume to be further satisfied after any supply from predetermined disturbances. | remain_irw_harvest= harvest_irw_vol- irw_predetermined remain_fw_harvest= harvest_fw_vol-fw_predetermined |

## Стр. 23

20 
Satisfying fully the IRW expected harvest 
tot_irw_vol_avail 
tot_fw_vol_avail 
The annual total volume that is eligible 
to be harvested in the time step 
according to the applicable silvicultural 
practices and the “market factor”. 
tot_irw_vol_avail = Σ irw_avail (see 
events.csv, see Table 13) 
tot_fw_vol_pot = Σ fw_avail (see 
events.csv, see Table 13) 
Satisfying fully the FW expected harvest 
still_remain_fw_vol 
The annual total volume of FW which 
was not satisfied from salvage logging 
and as collateral to IRW production. 
This amount should be satisfied 
through 
specific 
FW 
dedicated 
silvicultural 
interventions 
(i.e. 
disturbances classified as “fw_only” in 
events_templates.csv). 
still_remain_fw_vol 
= 
harvest_fw_vol - remain_fw 
 
The events.csv provides explicit results of HAT processing at the spatial resolution corresponding to the most 
detailed combination of classifiers, silvicultural interventions, and age, for each time step during the simulated 
period (calibration period excluded) (Table 17). 
Table 17. Definitions of the disaggregated indicators from events.csv. The measurement unit for these indicators is 
volume under-bark (m3) unless reported otherwise for the specific indicator (see proportions or amount). 
Indicator  
Description 
Formulas 
irw_pot  
fw_pot 
Total standing volume of IRW and FW potentially 
available, i.e. eligible, to be removed assuming 
applicable silvicultural rules and constraints in the 
time step, before the application of market factor. 
 
irw_avail 
fw_avail 
Total standing volume of IRW and FW potentially 
available to be removed assuming applicable 
silvicultural rules and constraints in the time step 
and modified by the market factor. 
irw_avail = irw_pot * 𝛾 𝑚𝑎𝑟𝑘𝑒𝑡 
(see 4 Distribute the expected 
harvest: harvest allocation tool 
(HAT)) 
irw_norm 
Proportion of IRW available for a particular 
combination 
of 
classifiers 
and 
silvicultural 
practices compared to the total IRW available, i.e. 
eligible, in the time step. 
irw_norm (%) = irw_avail/Σ 
irw_avail 
irw_need 
Target volume of IRW to be removed from each 
forest 
corresponding 
to 
a 
combination 
of 
classifiers and silvicultural interventions for the 
respective time step. 
remain_irw = Σ irw_need 
irw_frac 
The impact of removed IRW in irw_avail, i.e. the 
proportion (%) that is actually removed from the 
standing volume available in the time step. It has 
general information purpose, i.e. for assessing the 
target supply vs. availability. 
 
fw_colat 
The amount of FW collateral to IRW production, i.e. 
the amount of fuelwood which is expected from 
(see 4 Distribute the expected 
harvest: harvest allocation tool

*Таблица 23.1:*

| Satisfying fully the IRW expected harvest |  |  |
|---|---|---|
| tot_irw_vol_avail tot_fw_vol_avail | The annual total volume that is eligible to be harvested in the time step according to the applicable silvicultural practices and the “market factor”. | tot_irw_vol_avail = Σ irw_avail (see events.csv, see Table 13) tot_fw_vol_pot = Σ fw_avail (see events.csv, see Table 13) |
| Satisfying fully the FW expected harvest |  |  |
| still_remain_fw_vol | The annual total volume of FW which was not satisfied from salvage logging and as collateral to IRW production. This amount should be satisfied through specific FW dedicated silvicultural interventions (i.e. disturbances classified as “fw_only” in events_templates.csv). | still_remain_fw_vol = harvest_fw_vol - remain_fw |

*Таблица 23.2:*

| Indicator | Description | Formulas |
|---|---|---|
| irw_pot fw_pot | Total standing volume of IRW and FW potentially available, i.e. eligible, to be removed assuming applicable silvicultural rules and constraints in the time step, before the application of market factor. |  |
| irw_avail fw_avail | Total standing volume of IRW and FW potentially available to be removed assuming applicable silvicultural rules and constraints in the time step and modified by the market factor. | irw_avail = irw_pot * 𝛾 𝑚𝑎𝑟𝑘𝑒𝑡 (see 4 Distribute the expected harvest: harvest allocation tool (HAT)) |
| irw_norm | Proportion of IRW available for a particular combination of classifiers and silvicultural practices compared to the total IRW available, i.e. eligible, in the time step. | irw_norm (%) = irw_avail/Σ irw_avail |
| irw_need | Target volume of IRW to be removed from each forest corresponding to a combination of classifiers and silvicultural interventions for the respective time step. | remain_irw = Σ irw_need |
| irw_frac | The impact of removed IRW in irw_avail, i.e. the proportion (%) that is actually removed from the standing volume available in the time step. It has general information purpose, i.e. for assessing the target supply vs. availability. |  |
| fw_colat | The amount of FW collateral to IRW production, i.e. the amount of fuelwood which is expected from | (see 4 Distribute the expected harvest: harvest allocation tool |

## Стр. 24

21 
fully satisfying the IRW harvest. 
(HAT) 
fw_norm 
Proportion (%) of standing volume of FW available 
for a particular combination of classifiers and 
silvicultural practices compared to the total FW 
available, considering only fuelwood dedicated 
silvicultural practices, i.e. defined as “fw_only” in 
the events_templates.csv. 
fw_norm (%) = fw_avail/Σ 
fw_avail 
fw_need 
Target volume of FW satisfied by the application 
of FW dedicated silvicultural practices. 
 
amount 
Target amount of carbon (in tons of C) to be 
removed 
from 
forest 
corresponding 
to 
a 
combination 
of 
classifiers 
and 
silvicultural 
interventions for the respective time step. Notably, 
HAT converts any type of input to mass (carbon) 
targets, e.g. natural disturbances input may be 
defined in terms of area. 
Amount = irw_need * wood 
density * Cfraction  
(see 4 Distribute the expected 
harvest: harvest allocation tool 
(HAT) 
3.8 Exploration of EU-CBM-HAT results 
EU-CBM-HAT does not have a graphical user interface. It delivers output data in the form of Pandas data 
frames, a standard data science tool which opens a wide range of data manipulation, plotting and automation 
possibilities. Moreover, there is not a unique result file, so to analyse C stocks, C fluxes and related events, all 
output .csv files must be merged upon common keys. To facilitate this merge, eu_cbm_hat provides, with the 
installation, a script which aggregates simulation results in a unique data frame and parquet file, making it 
available for further data processing through any data science software 
The exploration scripts used by the team during the EU-CBM-HAT development are all available for download 
at the installation from: https://gitlab.com/bioeconomy/eu_cbm. 
3.9 Creating a new combination of scenarios 
With the installation, a dataset called “reference” scenario for a mock country ZZ is provided as the default 
version of input data.  
In order to run a new combination of scenarios, they should be defined using a text editor following the steps 
in Table 18. The existing files associated with the reference scenario can be used as templates for the new 
scenario. 
Table 18. Steps to define a new combination of scenarios, ZZ is the name of a mock country 
File location and description 
Default templates 
Add data specific to the “new_scenario” in 
each relevant input file. The assumptions have 
to be identified as “new_scenario” on the 
column “scenario” across all files. The time 
series has to start with the year simulated by 
the HAT, e.g. 2021, if the calibration period 
finished 2020. 
For example, in case of a new scenario for afforestation, 
specific 
records 
must 
be 
added 
in: 
events.csv, 
growth_curves.csv, inventory.csv, transitions.csv. in ...\ 
eu_cbm_data\countries\ZZ\activities\afforestation.  
Also, information specific to the new assumptions must 
be added in the following files contained in the other 
directory (as explained above in Lower level of the EU-
CBM-HAT: country specific inputs): 
eu_cbm_data\countries\ZZ\common 
- 
on 
the 
new 
disturbance types; 
eu_cbm_data\countries\ZZ\config - for the changes in the 
AIDB and association file;

*Таблица 24.1:*

|  | fully satisfying the IRW harvest. | (HAT) |
|---|---|---|
| fw_norm | Proportion (%) of standing volume of FW available for a particular combination of classifiers and silvicultural practices compared to the total FW available, considering only fuelwood dedicated silvicultural practices, i.e. defined as “fw_only” in the events_templates.csv. | fw_norm (%) = fw_avail/Σ fw_avail |
| fw_need | Target volume of FW satisfied by the application of FW dedicated silvicultural practices. |  |
| amount | Target amount of carbon (in tons of C) to be removed from forest corresponding to a combination of classifiers and silvicultural interventions for the respective time step. Notably, HAT converts any type of input to mass (carbon) targets, e.g. natural disturbances input may be defined in terms of area. | Amount = irw_need * wood density * C fraction (see 4 Distribute the expected harvest: harvest allocation tool (HAT) |

*Таблица 24.2:*

| File location and description | Default templates |
|---|---|
| Add data specific to the “new_scenario” in each relevant input file. The assumptions have to be identified as “new_scenario” on the column “scenario” across all files. The time series has to start with the year simulated by the HAT, e.g. 2021, if the calibration period finished 2020. | For example, in case of a new scenario for afforestation, specific records must be added in: events.csv, growth_curves.csv, inventory.csv, transitions.csv. in ...\ eu_cbm_data\countries\ZZ\activities\afforestation. Also, information specific to the new assumptions must be added in the following files contained in the other directory (as explained above in Lower level of the EU- CBM-HAT: country specific inputs): eu_cbm_data\countries\ZZ\common - on the new disturbance types; eu_cbm_data\countries\ZZ\config - for the changes in the AIDB and association file; |

## Стр. 25

22 
eu_cbm_data\countries\ZZ\silv 
– 
description 
of 
the 
silvicultural practices and wood use. 
Add data on IRW and FW expected harvest in 
the new directory. 
irw_ harvest.csv, fw_harvest.csv, rw_harvest.csv in the 
directory eu_cbm_data\domestic_harvest\new_scenario. 
Compile a new .yaml file with the combination 
of scenarios desired. NB. A .yaml file is a 
configuration file that can be edited with a 
text editor. 
Create 
a 
new 
file 
in 
eu_cbm_hat\combos: 
new_scenario.py. 
Create 
a 
new 
class 
and 
import 
the 
corresponding module in the file __init__.py in 
...\eu_cbm_hat\combos of the eu_cbm_hat. 
Add the new class [...new_scenario...] and import the new 
module [...new_...] in __init__.py, by paying attention to 
consistency of names, e.g. class name: “New_scenarios”, 
short_name: “new_scenarios”.

*Таблица 25.1:*

|  | eu_cbm_data\countries\ZZ\silv – description of the silvicultural practices and wood use. |
|---|---|
| Add data on IRW and FW expected harvest in the new directory. | irw_ harvest.csv, fw_harvest.csv, rw_harvest.csv in the directory eu_cbm_data\domestic_harvest\new_scenario. |
| Compile a new .yaml file with the combination of scenarios desired. NB. A .yaml file is a configuration file that can be edited with a text editor. | Create a new file in eu_cbm_hat\combos: new_scenario.py. |
| Create a new class and import the corresponding module in the file __init__.py in ...\eu_cbm_hat\combos of the eu_cbm_hat. | Add the new class [...new_scenario...] and import the new module [...new_...] in __init__.py, by paying attention to consistency of names, e.g. class name: “New_scenarios”, short_name: “new_scenarios”. |

## Стр. 26

23 
4 Distribute the expected harvest: harvest allocation tool (HAT)  
4.1 HAT concept 
HAT represents EU-CBM-HAT’s own module for the distribution of the roundwood expected harvest according 
to the simultaneous availability of IRW and FW from applicable silvicultural practices in eligible stands. 
Conceptually, to allocate the IRW and FW harvests, HAT estimates the roundwood amount that ca be virtually 
harvested in a time step based on total availability in the eligible pools from the eligible stands defined 
according to predefined silvicultural practices criteria.   
This solution is consistent with the forest management approach where decisions regarding harvesting 
amount are mostly based on the availability in the standing stock, within the sustainability criteria applicable 
by country’s forestry. This approach is also taken due to type of data run internally by libcbm, i.e. amount of C 
stock in the standing pools. Meanwhile, other approaches may consider the ratio of harvest over the annual 
increment (e.g. Government Offices of Sweden, 2019; Department of Agriculture, Food and the Marine Ireland, 
2019), or various threshold parameters, e.g. based on the diameter or areas, applied individually or in 
combination (e.g. Ministry of Agriculture and Forestry Finland, 2019). 
In distributing the harvests, HAT applies the same rules regarding silvicultural practices as libcbm will in the 
actual simulation. These rules include: 
(i) 
the definition of the standing pools targeted to provide a certain contribution to the harvest;  
(ii) 
the definition of the age ranges when respective silvicultural practices can be applied;  
(iii) 
the period of expected return to the same stand for the following silvicultural intervention, and,  
(iv) 
the type of product expected from a silvicultural intervention (“IRW and FW”, or “FW only”).  
In defining the availability of roundwood for harvesting, HAT simultaneously checks the eligible fluxes to the 
wood product pool from four standing pools, i.e. merchantable over-bark (o.b.), other woody components, stem 
snags and branch snags. The availability is given as a combination of the characteristics of each silvicultural 
practice (e.g. intensity of removals for relevant pools) and pools’ status (e.g. the removable quantity and 
expected quality of roundwood). The expected quality of roundwood removals refers to the share of IRW in 
the total roundwood removal to result from that type of silvicultural intervention (see Table 6) . This approach 
makes HAT to mimic the real-life process, where the amount of harvest provided from a stand always contain 
a fraction that only can be used for energy (e.g. Routa et al., 2012; Ikonen et al., 2003; Bosela et al., 2016; 
Węgiel et al., 2018; Jansone et al., 2017; Ruter, 2021; Schulze et al., 2022). This is more insightful than simply 
assessing the roundwood amount available as a merchantable standing stock is only designed for IRW or FW. 
This approach attempts to improve the link between roundwood quality and silvicultural interventions. 
HAT assesses the availability and distributes wood harvest into silvicultural practices in every time step, at the 
detail defined by the combination of classifiers. The assessment of the roundwood availability and distribution 
of expected harvest is completed only after the natural disturbances and associated silvicultural operations 
have been pre-processed for each time step. Thus, the availability of standing timber stocks is the result of 
forest growth and natural disturbances, re-evaluated at the beginning of each time step.

## Стр. 27

24 
 
Figure 3. Representation of HAT procedure behind estimating the standing stocks availability and distribution of IRW and FW harvests, and the interaction between HAT and libcbm. Dotted 
lines represent the virtualizing of the silvicultural operations which define the events to be applied in a certain time step (t). The years mark a ‘calibration period’ and EU climate policy 
landmark years (e.g. 2020, 2050).

## Стр. 28

25 
HAT focuses on distributing IRW with priority over FW, while also targeting first the availability from salvage 
logging over silvicultural practices. This capability is implemented through the three consecutive steps (Figure 
3) as follows: 
Step 1: estimate the expected amounts of IRW and FW available from predetermined disturbances in 
the time step t, i.e. salvage logging from natural disturbances and deforestation, as well as any 
predefined silvicultural intervention (e.g. clear cut defined as area, if needed). This means that HAT first 
implements the silvicultural practices associated with disturbances which typically result in salvage 
logging (i.e. natural disturbances and deforestation). 
Step 2: estimate the expected amount of IRW provided through silvicultural practices associated with 
salvage logging in the year after the natural disturbance events and regular silvicultural practices in 
the stands available in the respective time step t, e.g. all the stands not subject to predetermined 
disturbances or to other silvicultural restrictions, like e.g. time elapsed since the last silvicultural 
intervention, as described in the events_templates.csv. In this phase, HAT distributes only the 
difference between the total IRW harvest and the IRW to be provided as of Step 1. Given the standing 
roundwood quality and wood exploitation efficiency, some FW amount would inherently result as 
collateral FW, which together with FW from salvage logging would contribute to reach the FW harvest.  
Step 3: estimate the remaining amount needed to fully satisfy the FW expected harvest, according to 
the availability of roundwood from stands where fuelwood dedicated silvicultural practices may take 
place, e.g. such as pre-commercial thinning, coppices, as described in the events_templates.csv. 
The amounts of IRW and FW acquired from all three steps are cumulated and then passed to libcbm for the 
actual running of the respective time step t. In case the expected harvest is not satisfied in one time step, 
explicit messages are issued while the output files provide for all the relevant quantities (see 6 Automatic 
checks of the input data and error messages during the runs). 
4.2 Treatment of salvage logging 
HAT accounts the salvage logging first, before allocating the expected harvest. Specifically, HAT can account 
for the salvage logging in one or several successive time steps, as follows:   
"One-year-go” when both the natural disturbance event and the salvage logging associated with it 
occur in the same time step, so a direct transfer from living biomass pool, i.e. from “merchantable” to 
“products” is defined via the AIDB’s disturbance matrix. This is implemented as part of predetermined 
disturbances in Step 1 above;  
"Multiple-years-go", when the natural disturbance event is applied in one time step and salvage logging 
in two or more subsequent time steps. For the time step of the disturbance event there is a transfer of 
affected live biomass to dead organic matter pools (i.e. to stem snags). Then, in the following time step(s) a 
fraction from “dead organic matter” pools will be transferred to the “product” pools through annual 
silvicultural practices corresponding to salvage logging(s) operations. This is implemented as part of 
silvicultural practices in Step 2 above.  
4.3 Distribution of the industrial roundwood and fuelwood harvests 
HAT performs a volume-based allocation of the roundwood harvest based on the standing availability of IRW 
and FW across eligible resources. Eligibility is defined by a specific combination of classifiers, applicable 
silvicultural practices and other constraints (e.g. period since last intervention, coniferous and broadleaves 
share of IRW in the expected roundwood removal).  
The following pattern of calculation is used by HAT to calculate the amount of roundwood to be harvested 
within the time step t.  
To distribute the roundwood harvests across applicable silvicultural practices HAT operates all internal 
calculations as volume under-bark.  
On HAT side, the expected harvests are formulated as volume under-bark while the internal processing of 
libcbm is defined as over-bark. HAT does the conversion with two parameters: the bark fraction 𝑏 and the 
basic wood density 𝜌. Expected basic wood density is the ratio between oven-dry mass (at 0% moisture) and 
green volume (water-saturated wood volume, i.e. fresh state) in g/cm3 (e.g. Vieilledent et al., 2018). The 
relationship between the under-bark volume 𝑉𝑢𝑏 and the over-bark volume V𝑜𝑏 is expressed as:

## Стр. 29

26 
𝑉𝑢𝑏= 𝑉𝑜𝑏∗(1 −𝑏) 
 
Eq. (1) 
or 
𝑉𝑜𝑏=
𝑉𝑢𝑏
(1−b)  
 
Eq. (2) 
On the libcbm side, the C stocks simulated at the end of the previous time step (t-1) and C fluxes associated 
with predetermined disturbances virtualized for time step t, are first converted to volume under-bark (i.e. the 
same unit used as for IRW and FW harvests) according to the following steps. 
The carbon in any pool, i.e. merchantable biomass (Mob), expressed in terms of C, as simulated by libcbm, is 
converted to the volume over bark: 
𝑀𝑜𝑏= 𝑉𝑜𝑏∗𝜌∗0.49 
 
Eq. (3) 
where: 
0.49 is assumed as a constant carbon fraction of wood material (IPCC, 2006).  
Further on, the volume under-bark can be calculated from the libcbm’s C stocks and fluxes with this generic 
equation:  
𝑉𝑢𝑏=
𝑀𝑜𝑏
𝜌∗0.49 ∗(1 −𝑏) 
 
Eq. (4) 
In order to estimate the amount of roundwood potentially available, HAT applies Eq. 4 to fluxes to products 
from predetermined disturbances and to the eligible stocks of four eligible pools in the eligible stands. As a 
general rule, the available amount of IRW in the four pools for each set of classifiers 𝑖 and disturbance event 
d, in time step 𝑡, is annualized by dividing the part of the eligible standing stocks to be moved to product’s 
pool by the disturbance event d, by the return period σ (i.e. the “bias” defined as the minimum number of 
years between two consecutive disturbance events affecting the same stand, as defined within the 
events_template.csv). Eventually, the annualized availability is further modified by an annual market factor 𝛾 
taking into account possible further deviations due to specific market contingencies. Therefore, for a specific 
silvicultural practice d applied to a combination of classifiers i, the amount of biomass potentially available as 
IRW at the time step t (𝑀𝑎𝑣𝑖,𝑑
𝑡 in tC) is estimated as:  
𝑀𝑎𝑣𝑖,𝑑
𝑡
=
𝑀𝑖,𝑑
𝑡−1∗𝑓𝑑
𝜎
∗𝑓𝐼𝑅𝑊  
Eq. (5) 
where:  
𝑀𝑖,𝑑
𝑡−1 is the total amount of the standing stocks in the eligible pools for the relevant combination of 
classifiers extracted from libcbm output for the time step (t-1), in the eligible age range attributed to the 
silvicultural practice d (as defined within the event_templates.csv), applied to the classifiers’ combination i;  
fd is the share (%) of standing stock in the eligible pools moved to the product pool through the 
specific silvicultural intervention d, according to the matrix defined within the AIDB (e.g. 85% of the stems and 
50% of the stem snags, for a final cut); 
σ is the return period assigned to disturbance event d (in years). In a sustainably managed forest in 
Europe, tending or harvest in a specific stand takes place once in about 10 years (e.g. Schall and Ammer, 
2013; Schulze et al., 2022); 
fIRW  is the share (%) of roundwood of industrial quality from the roundwood amount to be removed 
from the forest (according to the input defined in file irw_frac_by_dist.csv).  
Once 𝑀𝑎𝑣𝑖,𝑑
𝑡 is estimated for each applicable disturbance event d, it is converted to roundwood volume 
under-bark available for harvesting within the time step t (𝑉𝑎𝑣𝑖,𝑑
𝑡 in m3 u.b.) through Eq. (4): 
By performing this operation for all applicable silvicultural practices and classifiers’ combinations, HAT 
estimates the total potential roundwood volume available in the time step t. For each time step, the sum of 
all volumes represents the total potentially available in the time step, while the proportion of participation of 
each silvicultural practice allows distributing the harvest proportionally across availability. Specifically, HAT 
calculates the corresponding normalized values, or the fraction of available roundwood (𝐹𝑖𝑟𝑤𝑖,𝑑
𝑡) in the total 
as the sum of all available volumes, for a given silvicultural practice d for each forest type, applied to a set of 
classifiers 𝑖, within the time step t, as follows:

## Стр. 30

27 
𝐹𝑖𝑟𝑤𝑖,𝑑
𝑡
=
𝑉𝑎𝑣𝑖,𝑑
𝑡
∑𝑉𝑎𝑣𝑖,𝑑
𝑡  
 
Eq. (6) 
The harvest is finally distributed amongst different classifiers and silvicultural intervention events according 
to the corresponding fraction estimated within Eq. (6). The proportions should sum to one for a time step. 
Such an approach allows to estimate the potential contributions of each silvicultural intervention assuming a 
strict application of the forest management rules through defined silvicultural practices. Still, different 
exogenous scenarios, e.g. energy or economic, or other forest management scenarios, may require a deviation 
from this pattern. For this reason, a market skew factor (𝛾) allows modifying such allocation. In this case a 
deviation 'harvest factor’ is used instead of using the normalized value F generated from Eq. (7), as follows:  
𝐹𝑖,𝑑,𝑚𝑎𝑟𝑘𝑒𝑡
𝑡
= 
𝑉𝑖,𝑑
𝑡
𝛴𝑉𝑖,𝑑
𝑡 * ϒ𝑚𝑎𝑟𝑘𝑒𝑡 
 
Eq. (7) 
where: 
𝛾market is a factor adjusting the proportion of actual roundwood amount distributed on a combination 
of classifiers. The proportions should sum to one for a given product (IRW or FW) and a given time step t, in 
order to avoid modifying the target harvest. Assuming the market demand is different from the available 
proportion of coniferous and broadleaves in the eligible stands, 𝛾market can be used to allocate a higher 
roundwood harvest to the coniferous stands.  
𝛾market is exogenously defined as a fraction in the harvest_factors.csv file. The data input for 𝛾market 
addresses the IRW harvest, while no market factor is applied for FW, meaning that HAT distributes the FW 
expected harvest along all classifiers proportionally to the available stock in eligible stands under the 
applicable FW-dedicated silvicultural practices. 
𝛾market can be applied on coniferous and broadleaves as default version, or alternatively, on forest 
types and silvicultural practices. The application of these options is automatically implemented by HAT, and 
simply depends on how harvest factor data is filled in in the harvest_factor.csv. 
The default version of the EU-CBM-HAT assumes the market factor is implemented on the grouping of 
coniferous and broadleaves, as the most aggregated indicator of the market influence. In doing this, first, HAT 
estimates the proportion of each group of conifers and broadleaves in the total annualized available volume 
under-bark (Eq.8) by summing the proportions F corresponding to original contribution for each forest type 
and silvicultural disturbance event (as of Eq. 6). The aggregation of normalized values by group is written as 
follows:   
∑
𝐹𝑖,𝑑
𝑡
𝐶𝑜𝑛
+ ∑
𝐹𝑖,𝑑
𝑡
𝐵𝑟𝑜𝑎𝑑
 = 1   
Eq. (8) 
where: 
F is the aggregated fraction for each of the two groupings, estimated by HAT as the sum of the 
actual contribution of each forest type and silvicultural practice within the coniferous and broadleaves groups 
in the year t, non-dimensional. 
Then, the HAT joins the user-defined expected proportion ϒ for the coniferous and broadleaves groups, for 
each time step t during the simulation. The sum of the harvest factors in harvest_factor.csv has to respect the 
rule: 
ϒ𝑖,𝑑 𝐶𝑜𝑛
𝑡
+ ϒ𝑖,𝑑 𝐵𝑟𝑜𝑎𝑑
𝑡
= 1  Eq. (9) 
The original proportion of participation for each forest type and silvicultural practices is then modified 
internally by HAT, as example for coniferous: 
𝐹𝑖𝑟𝑤𝑖,𝑑 𝑎𝑝𝑝𝑙𝑖𝑒𝑑
𝑡
 = 𝐹𝑖𝑟𝑤𝑖,𝑑
𝑡
ϒ𝑖,𝑑 𝐶𝑜𝑛
𝑡
∑
𝐹𝑖𝑟𝑤𝑖,𝑑
𝑡
𝐶𝑜𝑛
   
Eq. (10) 
where: 
𝐹𝑖𝑟𝑤𝑖,𝑑
𝑡 - fraction estimated for each silvicultural practice for each forest type within coniferous and 
broadleaved groups, according to Eq. (6). 
Further on, the harvest is redistributed taking into account the adjusted F values (Eq. 11), as follows:

## Стр. 31

28 
 
𝐷𝑖,𝑑
𝑡
= 𝐷∗ 𝐹𝑖𝑟𝑤𝑖,𝑑 𝑎𝑝𝑝𝑙𝑖𝑒𝑑
𝑡
  
Eq. (11) 
where: 
D – harvest under-bark for each silvicultural practice for each forest type. 
The alternative version to default one assumes that, instead of aggregation of coniferous and broadleaved 
groupings, EU-CBM-HAT allows implementing a modified contribution on each silvicultural operation on each 
forest type. The expected values of the market factors have to be exogenously generated and introduced in 
harvest_factor.csv, detailed specifications of harvest factor values. In this case, the default value is equal to 
1. If modulation is needed, the values should be modified in a way that would consider keeping the harvest 
quantity at the same level.   
Further on, HAT estimates the production of FW collateral to IRW production from the virtualization of the 
regular silvicultural practices designed to satisfy IRW, as such silvicultural practices are labelled as “IRW and 
FW” in events_template.csv. The collateral FW is estimated at the same level of detail to which the IRW 
availability is calculated, as follows: 
 
𝑓𝐹𝑊𝑖,𝑑
𝑡   = 1 −𝑓𝐼𝑅𝑊𝑖,𝑑
𝑡 
Eq. (12) 
where: 
fIRW - share of industrial roundwood in removals associated with silvicultural practices on combination 
of classifiers as of irw_frac_by_dist.csv. 
Finally, any remaining unsatisfied amount of fuelwood harvest, i.e. after deducting FW from salvage logging 
and collateral FW, is satisfied from fuelwood dedicated silvicultural practices (labelled as “FW_only” in 
events_template.csv). The availability of FW is calculated in the same way as IRW (i.e. Eq.1 to Eq.6), assuming 
that the harvest is distributed following a fraction-based allocation of availability across eligible combination 
of classifiers and stands. 
As the very last step, HAT prepares the events.csv input in the format required by SIT, by converting the 
under-bark volumes (m3) determined as harvestable in the time step to mass (tC) following backward the 
same procedure reported in (Eq. 4).  
4.4 Uncertainty and inconsistency in distributing the harvests 
Back and forth calculations through HAT (see 4.3 Distribution of the industrial roundwood and fuelwood 
harvests) for distributing the harvests and how eu_cbm_hat supplies that targeted amounts may result in 
some inconsistencies, as follows: 
— The estimates of IRW and FW associated with a certain silvicultural practice calculated by HAT and 
resulting from libcbm running represent different things. HAT estimates the average availability across 
applicable age range, so there are no target stands attached to these values. Meanwhile for libcbm the 
supplied amounts are attached to stands eligible as of the respective silvicultural practice, i.e. “older 
stands first” so selecting the stands with highest biomass first in distributing the expected harvest. The 
effect is expected to be negligible on the simulation results, although it may become relevant when the 
harvests target the maximum wood supply, e.g. not all standing availability may be captured. 
— The eu_cbm_hat uses two types of data for the conversion of biomass-to-volume under-bark, and vice 
versa. HAT uses two non-age dependent coefficients with constant value: the share of bark and the wood 
density (via input file: vol_to_mass_coefs.csv). Meanwhile, libcbm relies on age-dependent, non-linear 
volume-to-biomass equations (Boudewyn et al., 2006), because of the asynchrony of accumulation of 
standing biomass vs. merchantable volume or the actual proportion of non-stem compartments in total 
aboveground biomass vary during the age in general, e.g. influenced by the silvicultural practices. 
Because of the mismatch between these two types of data, inconsistency of the volume-to-biomass input 
or biomass-to-volume output may occur. To minimize such errors the strategy has to ensure full 
consistency between the values of the two types of data when sampled data is used (e.g. from NFIs), or 
when selecting the best match from the Canadian library of Boudewyn eqs. (as the table in AIDB when 
download and install CBM from https://www.nrcan.gc.ca/climate-change/climate-change-impacts-
forests/carbon-accounting/carbon-budget-model/13107). Since the shares of wood density and bark in

## Стр. 32

29 
total aboveground biomass vary with the age, a meaningful approach corresponds to looking to mature 
stands, i.e. older age classes (e.g. over 20-30 age) as far as the proportion of mature wood to entire stem 
wood is significant. This is expected to result in negligible effect on the projected estimates when 
appropriate input data and processing are involved. 
— The conversion of eu_cbm_hat outputs, i.e. C stocks and fluxes, to volume under-bark corresponding to 
the harvest is assuming the same conversion parameters for all standing pools subject to harvesting, i.e. 
stemwood, other wood components and snags. HAT uses the same conversion value for all assuming that 
any pool subject to harvesting has the same characteristics as living stemwood. This is supported by the 
fact that the decayed wood in advanced stages of decomposition is most likely not subject to harvesting, 
and in any case not for industrial roundwood. This is expected to have a negligible effect on the 
projections or harvest supply. 
— HAT converts the measurement type compared to actual input, given HAT is processing all inputs in terms 
of mass (M), but the impact on the simulation is negligible as HAT ensures full correspondence between 
volume-biomass-area-proportion.

## Стр. 33

30 
5 Calibration 
The EU-CBM-HAT allows executing a calibration, i.e. for the period for which historical data is available. The 
calibration period is specified by the “reference_year” which is the inventory's year, i.e. the first calibrated year 
is the following year after, and the “base_year”, which is the first simulated year, e.g. 2021. 
Unlike HAT which requires separate inputs for IRW and FW harvests, the calibration can be done on total 
roundwood harvest (i.e. the sum of IRW and FW). Nonetheless, different formulation of harvest targeted for 
calibration and simulated period may introduce a sudden change across all forest state indicators and 
roundwood removal structure, e.g. allocation between coniferous and broadleaved groupings or contribution of 
volumes or areas of the final cut and thinnings, for which reason additional checks are needed. Normally, the 
application of a harvest factor similar to calibration period should solve the problem.

## Стр. 34

31 
6 Automatic checks of the input data and error messages during the runs 
Inherently, mismatches may occur in setting up the databases, especially when new scenarios are set. EU-
CBM-HAT performs some automatic checks of consistency across input data (at least for the errors which 
were identified during the development and testing). Most of the checks are performed in the earliest stages 
of a simulation, in order to minimize the time lost by the user in fixing any error. Specifically, in case of 
inconsistent inputs, while the simulation will stop and print one of the following error messages (Table 19). 
Table 19. Messages printed by the EU-CBM-HAT in case of errors generated by inconsistent inputs (list is not exhaustive).  
Message 
Most likely explanation, and solution  
“Undefined 
classifier 
values 
detected: 
classifier: 'forest_type', values: ['PA']” 
The classifier list is missing one criterion which is used by 
other inputs. 
“missing classifiers combination” 
Inconsistent combination of classifiers among various inputs. 
“doubling 
the 
age 
ranges for 
various 
disturbances” 
events_template.csv contains multiple silvicultural practices 
which include overlaps in defining the applicable age range, 
instead successive with continuity or gap have to be defined. 
“columns must have matching elements 
counts” 
Mismatches within or between events_template.csv” and 
irw_frac_by_dist.csv. 
“Names 
don't 
match 
IDs 
in 
...\ 
_data\countries\ZZ\silv\events_templates.csv'”. 
NB. ZZ is the name of the country subject to 
simulation). 
Mismatch regards the combination of classifiers between 
disturbance_type.csv and events_templates.csv files. An 
explicit list of non-matching or missing information is 
provided in the editor. 
“The 
file 
...\eu_cbm_hat 
data\output\hat\ZZ\0\input\csv\classifiers.csv' 
has 1 empty lines”. 
Any of the input files contains an empty line. 
“Exception: There is remaining fw harvest this 
year: .... m3, but there are no events that 
enable the creation of FW only.”. 
Silvicultural practices targeting “fw_only” are missing from 
events_template.csv. 
“ValueError: You probably have two or more 
rows in your events file which both have the 
same classifier values. Hence one cannot 
convert it from wide to long format.” 
events.csv file contains repeated identical classifiers and 
disturbances, to remove the rows with identical combination. 
Sometimes, the simulation stops and an empty message is displayed as an AssertionError, i.e. something 
happen that the programmers thought impossible to occur. The first hint in finding the source of such error 
should be from identifying the stage where the simulation stopped. For example, when the message occurs 
after the editor displaying “INFO - Calling the cbm_simulator”, the error is most likely linked to inconsistencies 
in the input data, which were not identified by the automatic checks (in Table 5). If the error message is 
displayed after editor prints “INFO - Carbon pool initialization period is finished ... ” then the error is most likely 
related to HAT processing.  
In all cases of error messages, the editor prints a general message: “ERROR - Runner '.../ZZ/0' encountered an 
exception. See log file” – so directing the user to look for more information in the logfile 
“output/0/logs/runner.txt”. 
As the EU-CBM-HAT is under continuous development, more checks will be added regularly. Users are 
encouraged to submit test cases and new checks to the code repository.

*Таблица 34.1:*

| Message | Most likely explanation, and solution |
|---|---|
| “Undefined classifier values detected: classifier: 'forest_type', values: ['PA']” | The classifier list is missing one criterion which is used by other inputs. |
| “missing classifiers combination” | Inconsistent combination of classifiers among various inputs. |
| “doubling the age ranges for various disturbances” | events_template.csv contains multiple silvicultural practices which include overlaps in defining the applicable age range, instead successive with continuity or gap have to be defined. |
| “columns must have matching elements counts” | Mismatches within or between events_template.csv” and irw_frac_by_dist.csv. |
| “Names don't match IDs in ...\ _data\countries\ZZ\silv\events_templates.csv'”. NB. ZZ is the name of the country subject to simulation). | Mismatch regards the combination of classifiers between disturbance_type.csv and events_templates.csv files. An explicit list of non-matching or missing information is provided in the editor. |
| “The file ...\eu_cbm_hat data\output\hat\ZZ\0\input\csv\classifiers.csv' has 1 empty lines”. | Any of the input files contains an empty line. |
| “Exception: There is remaining fw harvest this year: .... m3, but there are no events that enable the creation of FW only.”. | Silvicultural practices targeting “fw_only” are missing from events_template.csv. |
| “ValueError: You probably have two or more rows in your events file which both have the same classifier values. Hence one cannot convert it from wide to long format.” | events.csv file contains repeated identical classifiers and disturbances, to remove the rows with identical combination. |

## Стр. 35

32 
7 Conclusions 
EU-CBM-HAT provides CO2 removals and emissions simulations related to forest management in support of 
EU climate law and GHG mitigation policies. It allows for the calibration at the national scale for the historical 
period against the national statistics reported internationally or nationally.  
One of the main strengths consists in its ability to easily combine unlimited number of scenarios for any 
management and exogenous events (as natural disturbances, market demands for industrial roundwood and 
fuelwood) occurring throughout simulation period, and for handy tracking and referencing them.  
Another major strength is a module distributing the harvest according to the simultaneous availability of IRW 
and primary FW from eligible silvicultural practices associated with standing stocks in merchantable wood, 
other wood components, stem and branch snags. 
This report is intended as a scientific and technical background of EU-CBM-HAT development and is 
complementary to the CBM-CFS3 user’s guide (Kull et al., 2019). 
One major limitation of EU-CBM-HAT is related to libcbm requirement of a very specific format of volume-to-
biomass equation which is a format unavailable for EU countries, i.e. which rely on expansion factors applied 
to standing stocks volume or individual tree allometry expanded to stand scale. In order to make these 
measurements available, collaborative activities, e.g. with NFIs, may be planned for the future. 
Another limitation may be that exogenous data is required for natural disturbances and forest land 
conversions, there is no development expected on these issues. 
Further and deeper integrations of EU-CBM-HAT within the JRC’s AFOLU modelling framework are expected. 
Upstream integration is expected with models on energy e.g. POTEnCIA (Mantzos et al., 2016) or economic 
models, e.g. CAPRI (Modelling System, 2022). Further downstream integration with a wood use and wood 
products carbon storage model, wood products recycling and wood substitution of energy and carbon 
intensive materials, i.e. with GFTM (Global Forest Trade Model, e.g. Jonsson et al., 2015) or GFPM (Global 
Forest Production Model, Buongiorno et al., 2003). Deeper elaboration of roundwood harvest on industrial 
roundwood and fuelwood would make EU-CBM-HAT suitable for assessing the economic linkages of different 
forest management options and actual wood use based on roundwood grading.  
EU-CBM-HAT is in essence a non-spatial, but a spatially referenced model. This means that during the 
simulation the original spatial structure maybe lost, although the representation of forest management 
remains realistic at aggregated scale. Consistent with the geo-spatial version, the Generic Carbon Budget 
Model (GCBM) launched by NRCAN (e.g. Shaw et al., 2021), or independently, a spatially explicit version can be 
the following development step, e.g. by linking it with EU biomass maps (European Commission, 2020). 
Nevertheless, a major difficulty to overcome in applying a spatial explicit version is the availability of data for 
the initial year of the simulation (i.e. standing volume at an adequate resolution to represent forest status and 
management interventions). 
Although EU-CBM-HAT was developed for further use by the JRC, the goal is to make it available and 
accessible to others outside the JRC. It can be applied both for GHG reporting and accounting (e.g. including 
annual time steps, all C pools, etc.) and for simulating different forest management and climate mitigation 
scenarios, both at EU or EU member state level. EU-CBM-HAT is freely available to any user, while the current 
version allows for refinement and adjustments, as needed. Updates are documented on the software source 
page. The model is in continuous operational development, while currently used to set up databases for an 
eventual EU “forest management reference scenario”, i.e. incorporating data for pre-2020.  Following 
Technology Readiness Levels (TRL) grading (European Commission, 2017), the current released version of EU-
CBM-HAT falls under TLS 8 (System complete and qualified) and TLS 9 (Actual system proven in operational 
environment).

## Стр. 36

33 
References 
Arets E. J. M. M., and Schelhaas M., 2019. National Forestry Accouting Plan: Submission of the Forest 
Reference Level 2021-2025 for the Netherlands. Ministerie LNV. https://edepot.wur.nl/513199 (last accessed 
09.08.2022). 
Berendt F., de Miguel-Diez F., Wallor E., et al., 2021. Comparison of different approaches to estimate bark 
volume of industrial wood at disc and log scale. Sci Rep 11, 15630 (2021). https://doi.org/10.1038/s41598-
021-95188-z (last accessed 09.08.2022). 
Blujdea V.N.B., Sikkema R., Dutca I., Nabuurs G.J., 2021. Two large-scale forest scenario modelling approaches 
for reporting CO2 removal: a comparison for the Romanian forests. Carbon Balance Manag. 2021 Aug 
21;16(1):25. doi: 10.1186/s13021-021-00188-1 (last accessed 09.08.2022). 
Bosela M., Redmond J., Kučera M., et al. Stem quality assessment in European National Forest Inventories: an 
opportunity 
for 
harmonised 
reporting?. 
Annals 
of 
Forest 
Science 
73, 
635–648 
(2016). 
https://doi.org/10.1007/s13595-015-0503-8.  
Böttcher H., Kurz W. A., and Freibauer A., 2008. Accounting of forest carbon sink and sources under a future 
climate protocol-factoring out past disturbance and management effects on age-class structure. For. Ecol. 
Manage, 11, 669–686, https://doi.org/10.1016/j.envsci.2008.08.005. 
Boudewyn P.A., Song X., Magnussen S., Gillis M.D., 2007. Model-based, volume-to-biomass conversion for 
forested and vegetated land in Canada. Nat. Resour. Can., Can. For. Serv., Pac. For. Cent., Victoria, BC. Inf. Rep. 
BC-X-411.   
Buongiorno J., Zhu S., Zhang D., Turner J., Tomberlin D., 2003. The Global Forest Products Model: Structure, 
Estimation, and Applications. ISBN 10: 0121413624 / ISBN 13: 9780121413620.  
Camia A., Robert N., et al., 2018. Biomass production, supply, uses and flows in the European Union: First 
results from an integrated assessment, EUR 28993 EN, Publications Office of the European Union, 
Luxembourg, 2018, ISBN 978-92-79-77236-8 (print), 978-92-79-77237-5 (pdf), doi:10.2760/539520, 
JRC109869. 
CAPRI Modelling System, 2022. Common Agricultural Policy Regionalised Impact Modelling System. 
https://www.capri-model.org/dokuwiki/doku.php?id=capri:capri_pub (last accessed 09.08.2022). 
Cuddington K., Fortin M. J., Gerber L. R., Hastings A., Liebhold A., O’connor M., Ray C., 2013. Process-based 
models are required to manage ecological systems in a changing world. Ecosphere, 4, 1–12, 
https://doi.org/10.1890/ES12-00178.1, 2013. 
Department of Agriculture, Food and the Marine, Ireland, 2019. Ireland’s National Forestry Accounting Plan 
2021-2025. 
Duffy P., Black K., Fahey D., Hyde B., Kehoe A., Murphy J., Quirke B., Ryan A.M., Ponzi J., 2021. National 
Inventory Report 2021 - greenhouse gas emissions 1990 – 2019 reported to the United Nations Framework 
Convention on Climate Change. Available at: https://www.epa.ie/publications/monitoring--assessment/climate-
change/air-emissions/ireland_nir-2021_cover.pdf (last accessed 09.08.2022). 
European Commission, 2016. POTEnCIA model description - version 0.9. EUR 27768. JRC100638 (last 
accessed: 09.08.2022). 
European Commission, 2017. Technology readiness levels (TRL). Extract from Part 19 - Commission Decision 
C(2014)4995. COMMISSION IMPLEMENTING DECISION amending Implementing Decision C(2013)8631 
adopting the 2014-2015 work programme in the framework of the Specific Programme Implementing Horizon 
2020 – The Framework Programme for Research and Innovation (2014-2020). Commission Decision 
C(2014)4995. 
Available 
at: 
https://ec.europa.eu/transparency/documents-
register/detail?ref=C(2014)4995&lang=en (last accessed: 09.08.2022). 
European Commission, Joint Research Centre, 2020. Forest Biomass Map of Europe. European Commission, 
Joint Research Centre [Dataset] PID: http://data.europa.eu/89h/d1fdf7aa-df33-49af-b7d5-40d226ec0da3 
(last accessed: 09.08.2022). 
European Commission, Joint Research Centre, 2021. Salvage loggings. European Commission, Joint Research 
Centre (JRC) [Dataset] PID: http://data.europa.eu/89h/2100b612-a4b0-4897-829b-72b7b1e5782c (last 
accessed: 09.08.2022).

## Стр. 37

34 
Gejdoš M. and Michajlová K., 2022. Analysis of Current and Future Forest Disturbances Dynamics in Central 
Europe. Forests 2022, 13, 554. https://doi.org/10.3390/f13040554. 
Government Offices of Sweden, 2019. National forestry accounting plan for Sweden. Revised 30 December 
2019. Ministry for the Environment Sweden.  
Grassi G., House J., Kurz W.A. et al., 2018. Reconciling global-model estimates and country reporting of 
anthropogenic forest CO2 sinks. Nature Clim Change 8, 914–920 (2018). https://doi.org/10.1038/s41558-
018-0283-x. 
Ikonen V.P., Kellomäki S., Peltola H., 2003. Linking tree stem properties of Scots pine (Pinus sylvestris L.) to 
sawn timber properties through simulated sawing. Forest Ecology and Management, Volume 174, Issues 1–3, 
2003, Pages 251-263. ISSN 0378-1127. https://doi.org/10.1016/S0378-1127(02)00035-X. 
IPCC, 2006. 2006 IPCC Guidelines for National Greenhouse Gas Inventories, Prepared by the National 
Greenhouse Gas Inventories Programme, Eggleston H.S., Buendia L., Miwa K., Ngara T. and Tanabe K. (eds). 
Published: IGES, Japan (last accessed: 09.08.2022). 
Jansone L., Dreimanis A., Kārkliņa A., Sisenis L., Adamovičs A., Puriņš M., 2017. Financial assessment of Fagus 
sylvatica stands in Latvia. 81-85. DOI: 10.22616/rrd.23.2017.012.  
Jevšenak J., Klopčič M., Mali B., 2020. The Effect of Harvesting on National Forest Carbon Sinks up to 2050 
Simulated 
by 
the 
CBM-CFS3 
Model: 
A 
Case 
Study 
from 
Slovenia. 
Forests, 
11, 
1090. 
https://doi.org/10.3390/f11101090. 
Jonsson R., Rinaldi F., San-Miguel-Ayanz J., 2015. The Global Forest Trade Model (GFTM) in the bioeconomy 
modelling framework, Joint Research Centre, Institute for Prospective Technological Studies, Publications 
Office, 2015, https://data.europa.eu/doi/10.2788/237058 (last accessed: 09.08.2022). 
Kull S.J., Rampley G.J., Morken S., Metsaranta J., Neilson E.T., Kurz W.A., 2019. Operational-scale Carbon 
Budget Model of the Canadian Forest Sector (CBM-CFS3) version 1.2: user’s guide. Nat. Resour. Can., Can. For. 
Serv., North. For. Cent., Edmonton, AB. (last accessed: 09.08.2022). 
Kurz W.A., Dymond C.C., White T.M., Stinson G., Shaw C.H., Rampley G.J., Smyth C., Simpson B.N., Neilson E.T., 
Trofymow J.A., Metsaranta J., Apps M.J., 2009. CBM-CFS3: A model of carbon-dynamics in forestry and land-
use change implementing IPCC standards, Ecological Modelling, Volume 220, Issue 4, 2009, Pages 480-504. 
ISSN 0304-3800. https://doi.org/10.1016/j.ecolmodel.2008.10.018. 
Luke, 
2021. 
Tukkipuun 
hakkuissa 
ennätykset 
rikki 
vuonna 
2021. 
Available 
at: 
https://www.luke.fi/fi/uutiset/tukkipuun-hakkuissa-ennatykset-rikki-vuonna-2021 (last accessed 08.11.2022). 
Skogsstyrelsen, 
2022. 
Avverkningen 
på 
rekordnivå 
2021. 
Available 
at: 
https://www.skogsstyrelsen.se/nyhetslista/avverkningen-pa-rekordniva-2021/ (last accessed 08.11.2022). 
Mantzos L., Wiesenthal T., Kourti I., Matei N., Navajas Cawood E., Papafragkou A., Rózsai M., Russ H., Soria R., 
2018. National Forest accounting plan of the Czech Republic, including a proposed forest reference level. 
Submission 
pursuant 
to 
Article 
8 
of 
Regulation 
(EU) 
2018/841. 
Available 
at: 
https://www.fern.org/fileadmin/uploads/fern/Documents/NFAP_Czech_Republic.pdf (last accessed 09.08.2022). 
Ministry of Agriculture and Forestry and Natural Resources Institute Finland, 2019. National Forestry 
Accounting Plan for Finland. Submission of updated National Forestry Accounting Plan including forest 
reference level (2021 – 2025) for Finland (20 December 2019).  
Ministry 
of 
Climate, 
Poland, 
2018. 
National 
Forestry 
Accounting 
Plan. 
Available 
at: 
https://www.gov.pl/attachment/3738b723-c2e4-472a-8f38-27df5641357e (last accessed 09.08.2022). 
Mubareka S., Vacchiano G., Pilli, R., Hilferink M., Fiorese G, Jonsson, R., Ruiz Castello P., Nijs W., Avitabile V., van 
Vliet J., Camia A., 2018. Integrated modelling approach to assess woody biomass supply, demand and 
environmental impacts of forest management in the EU 9th International Congress on Environmental 
Modelling and Software. Available at: https://scholarsarchive.byu.edu/iemssconference/2018/ (last accessed 
09.08.2022). 
Mubareka S., Jonsson R., Rinaldi F., Fiorese G., San-Miguel-Ayanz J., Sallnas, O., Baranzelli C., Pilli R., Lavalle C., 
Kitous A., 2014. An Integrated Modelling Framework for the Forest-based Bioeconomy. Available at: 
https://earthzine.org/an-integrated-modelling-framework-for-the-forest-based-bioeconomy/ 
(last 
accessed 
09.08.2022).

## Стр. 38

35 
Packalen T., Sallnaes O., et al., 2014. The European Forestry Dynamics Model: Concept, design and results of 
first case studies. Publications Office of the European Union, EUR 27004 doi: 10.2788/153990 (last accessed: 
09.08.2022). 
Pilli R., Grassi G., Kurz W. A., Smyth C. E., Blujdea V., 2013. Application of the CBM-CFS3 model to estimate 
Italy’s forest carbon budget, 1995 to 2020, Ecol. Model., 266, 144–171, doi:10.1016/j.ecolmodel.2013.07.007. 
Pilli P., Kull S.J., Blujdea V.N.B., Grassi G., 2018. The carbon budget model of the canadian forest sector (CBM-
CFS3): customization of the archive index database for European Union countries. Annals of forest science, 
75/3, p. 1-7. 
Pilli R., Alkama R., Cescatti A., Kurz W. A., & Grassi G., 2022. The European forest Carbon budget under future 
climate conditions and current management practices. Biogeosciences, 19(13), 3263-3284. 
Pretzsch H., Grote R., Reineking B., Rötzer T. H., Seifert S. T., 2008. Models for Forest Ecosystem Management: 
A European Perspective. Ann. Bot-London, 101, 1065–1087, https://doi.org/10.1093/aob/mcm246, 2008. 
Rinaldi F., Jonsson R., San-Miguel-Ayanz J., 2015. Fact sheet: the Global Forest Trade Model (GFTM) in the 
Bioeconomy modelling framework. Report JRC97272, https://publications.jrc.ec.europa.eu.  
Routa J., Kellomäki S., Strandman H., 2012. Effects of Forest Management on Total Biomass Production and 
CO2 Emissions from use of Energy Biomass of Norway Spruce and Scots Pine. Bioenerg. Res. 5, 733–747 
(2012). https://doi.org/10.1007/s12155-012-9183-5.  
Ruter S., 2021. Estimating and reporting of emissions/removals from living biomass/DOM and HWP associated 
with 
windthrow. 
JRC 
LULUCF 
virtual 
workshop 
2021. 
Available 
at: 
https://forest.jrc.ec.europa.eu/en/activities/lulucf/workshops/workshop-2021/ (last accessed: 09.08.2022). 
Sahoo A., Pérez-Domínguez I., Mubareka S., Fiorese G., Grassi G., Pilli R., Himics M., Blujdea V. N. B., Witzke P., 
Follador M., Neuwahl F., Salvucci R., Rozsai M., Kesting M (2021). Improved modelling framework for assessing 
the interactions between the energy, agriculture, forestry and land use change sectors: integrating the CAPRI, 
LUISA-BEES, CBM and POTEnCIA models, Publications Office. https://data.europa.eu/doi/10.2760/900305.  
Schall P. and Ammer C., 2013. How to Quantify Forest Management Intensity in Central European Forests. 
European Journal of Forest Research, 132, 379-396. https://doi.org/10.1007/s10342-013-0681-6. 
Schulze E.D., Bouriaud O., Irslinger R. et al. The role of wood harvest from sustainably managed forests in the 
carbon cycle. Annals of Forest Science 79, 17 (2022). https://doi.org/10.1186/s13595-022-01127-x. 
Shaw C.H., Rodrigue S., Voicu M.F. et al., 2021. Cumulative effects of natural and anthropogenic disturbances 
on the forest carbon balance in the oil sands region of Alberta, Canada; a pilot study (1985–2012). Carbon 
Balance Manage 16, 3 (2021). https://doi.org/10.1186/s13021-020-00164-1. 
Vieilledent G., Fischer F. J., Chave J., Guibal D., Langbour P., & Gérard J., 2018. New formula and conversion 
factor to compute basic wood density of tree species using a global wood technology database. American 
journal of botany, 105(10), 1653-1661. 
Verkerk P.J., Schelhaas M., Immonen V., Hengeveld G., Kiljunen J., Linder M., et al., 2016. Manual for the 
European 
Forest. 
Information 
Scenario 
model 
(EFISCEN 
4.1). 
Available 
at: 
https://efi.int/sites/default/files/files/publication-bank/2018/tr_99.pdf (last accessed: 09.08.2022). 
Vestin P, Mölder M, Kljun N, Cai Z, Hasan A, Holst J, Klemedtsson L, Lindroth A (2022). Impacts of stump 
harvesting on carbon dioxide, methane and nitrous oxide fluxes. iForest 15: 148-162. doi:10.3832/ifor4086-
015.  
Vizzarri M., Pilli R., Korosuo A. et al., 2021. Setting the forest reference levels in the European Union: overview 
and challenges. Carbon Balance Manage 16, 23 (2021). https://doi.org/10.1186/s13021-021-00185-4.  
Węgiel A., Bembenek M. Łacka, A. et al. Relationship between stand density and value of timber assortments: a 
case study for Scots pine stands in north-western Poland. N.Z. j. of For. Sci. 48, 12 (2018).

## Стр. 39

36 
List of abbreviations and definitions  
AFOLU 
Agriculture, Forestry and Other Land Use 
AIDB  
Archive Index Database 
C  
carbon 
C++ 
Programming language 
CBM 
short of CBM-CFS3 
CBM-CFS3 
Carbon Budget Model of the Canadian Forest Service 
CFS 
Canadian Forest Service 
COMBO 
scenario combination tool of the EU-CBM-HAT 
.csv 
Microsoft Excel comma separated value file 
CLU 
Climatic units 
Cur 
Volume data corresponding to increment tables 
DBH 
Diameter Breast Height 
EFISCEN  European Forest Information SCENario Model 
EU 
European Union 
EUPL 
European Union Public Licence 
FAOSTAT Food and Alimentation Organization statistics 
FW 
Fuel Wood 
GHG 
Greenhouse Gas 
GUI 
Graphical User Interface 
HAT 
Harvest Allocation Tool of the EU-CBM-HAT 
HWP 
Harvested Wood use type 
IRW 
Industrial Roundwood 
Init 
Volume data corresponding to yield tables 
JRC 
Joint Research Centre of the European Commission 
LUISA 
LUISA Territorial Modelling Platform 
LULUCF Land Use, Land Use Change and Forestry 
MIT  
Software licence by Massachusetts Institute of Technology 
MS 
Member State(s) of the European Union 
NFAP 
National Forestry Accounting Plan 
NFI 
National Forest Inventory 
NRCAN 
National Resources Canada/Ressources naturelles Canada 
nsr_nd 
Non-Stand Replacing Natural Disturbances 
o.b. 
over-bark 
OWC 
Other Woody Component 
POTEnCIA  
Policy Oriented Tool for Energy and Climate Change Impact Assessment 
QA/QC 
Quality Assurance, Quality Control 
SIT  
Standard Import Tool  
sr_nd  
Stand Replacing Natural Disturbances

## Стр. 40

37 
TRL  
Technology Readiness Levels  
UNECE 
United Nations Economic Commission for Europe 
u.b. 
under-bark 
UNFCCC  United Nations Framework Convention on Climate Change 
ZZ 
country example containing complete templates for all input data 
.yaml  
‘YAML Ain't Markup Language’ file type

## Стр. 41

38 
List of figures 
Figure 1. Upper architecture of the input data in the EU-CBM-HAT: overview of the mandatory directory and 
the files in the “data” directory. .................................................................................................................................................................................7 
Figure 2. Lower architecture of the input data in the EU-CBM-HAT:  overview of the directories and files 
included within each “country” directory (corresponding to box “Directory: countries” in Figure 1). ..............................9 
Figure 3. Representation of HAT procedure behind estimating the standing stocks availability and distribution 
of IRW and FW harvests, and the interaction between HAT and libcbm. Dotted lines represent the virtualizing 
of the silvicultural operations which define the events to be applied in a certain time step (t). The years mark 
a ‘calibration period’ and EU climate policy landmark years (e.g. 2020, 2050). .................................................................... 24

## Стр. 42

39 
List of tables 
Table 1. Main directories included within EU-CBM-HAT. ...........................................................................................................................8 
Table 2. Top-down description of the subdirectories included within each country-directory (detailed 
description in the following sections). ....................................................................................................................................................................9 
Table 3. Specific input files expected by libcbm’s SIT. ..............................................................................................................................9 
Table 4. Input required by the HAT module in distributing the harvest and constructing the “events” inputs. . 10 
Table 5. Description of the silvicultural practices as required by HAT in events_templates.csv. This table 
contains only the elements which are specific to EU-CBM-HAT, in addition to typical descriptors for “events” 
input required by libcbm, described in CBM-CFS3 User’s Guide (Kull et al., 2019). .............................................................. 11 
Table 6. Assumptions and default values regarding the fractions of industrial roundwood in the roundwood 
removals from forests (irw_fract_by_dist.csv). ........................................................................................................................................... 12 
Table 7. Input data for conversion of volume to biomass and bark fraction in standing volume in 
vol_to_mass_coefs.csv. ............................................................................................................................................................................................... 13 
Table 8. Files placed within the “config” directory. .................................................................................................................................. 14 
Table 9. Example of mapping of the input data with AIDB categories in associations.csv. The “name_input” is 
the name used for that respective category across the input data files, while the “name_aidb” is the name for 
the corresponding item in the AIDB. .................................................................................................................................................................... 14 
Table 10. Generic description of the content of the mandatory input for disturbance events. .................................. 14 
Table 11. Specific input data required for the conversion to forest............................................................................................. 15 
Table 12. Specific input data required for the conversion from forests.................................................................................... 16 
Table 13. Specific input data required for the natural disturbances. .......................................................................................... 17 
Table 14. Specific input data required for forest management, for both calibration and simulation period. ... 17 
Table 15. Output files of EU-CBM-HAT. .......................................................................................................................................................... 18 
Table 16. Definitions of the aggregated indicators as reported in extras.csv.  All values in this file are volume 
under-bark (m3) for the annual time step virtualized by HAT for the simulated period (calibration period 
excluded)............................................................................................................................................................................................................................... 19 
Table 17. Definitions of the disaggregated indicators from events.csv. The measurement unit for these 
indicators is volume under-bark (m3) unless reported otherwise for the specific indicator (see proportions or 
amount). ................................................................................................................................................................................................................................ 20 
Table 18. Steps to define a new combination of scenarios, ZZ is the name of a mock country ................................ 21 
Table 19. Messages printed by the EU-CBM-HAT in case of errors generated by inconsistent inputs (list is not 
exhaustive). ......................................................................................................................................................................................................................... 31

## Стр. 43

40 
Annexes 
Annex 1. EU-CBM-HAT installation instructions 
The software packages are under active development. Make sure to regularly update them to the latest 
version. This installation method will change, and the updated installation method will be made available in 
the repository: 
    https://gitlab.com/bioeconomy/eu_cbm/eu_cbm_hat. 
Install  EU-CBM-HAT using pip: 
    pip install git+https://gitlab.com/bioeconomy/eu_cbm/eu_cbm_hat.git   
Install the libcbm package developed by the Forest Carbon Accounting team of the Canadian Forest Service: 
    pip install git+https://github.com/cat-cfs/libcbm_py.git 
The Archive Index Databases (AIDB) can be quite large and that is why we put it in a separate git repository. 
Clone the repository containing the AIDB: 
    git clone git@gitlab.com:bioeconomy/eu_cbm/eu_cbm_aidb.git 
By default, the data is located in your home directory "~/repos/eu_cbm_data/" and the AIBD in 
“~/repos/eu_cbm_aidb/”, but you can define the following environment variables to tell the model where the 
data are located: 
    export EU_CBM_DATA="path_on_your_computer/eu_cbm_data/" 
    export EU_CBM_AIDB="path_on_your_computer/eu_cbm_aidb/" 
It is necessary to create symbolic links between the AIDB and the data repository. This can be achieved by 
entering the following at a python prompt:      
    from eu_cbm_hat.core.continent import continent      
    for country in continent: country.aidb.symlink_all_aidb() 
To run the test country ZZ at a Python prompt, see the version of the script that can run without eu_cbm_data 
at:  
    https://gitlab.com/bioeconomy/eu_cbm/eu_cbm_hat/-/tree/main/scripts/running 
As development of the package continues through time. It is recommended to regularly update both libcbm 
and eu_cbm_hat to the latest versions: 
    pip install --upgrade git+https://gitlab.com/bioeconomy/eu_cbm/eu_cbm_hat.git  
    pip install --upgrade git+https://github.com/cat-cfs/libcbm_py.git. 
 
Annex 2. Own test of consistency of libcbm and cbm-cfs3 
The libcbm requires the same input as CBM-CFS3 (see the CBM-CFS3 User’s Guide for further detailes). The 
CBM’s SIT works for both in the same way, and it accepts only data provided in a specific format.  
Existing EU database allowed testing the two versions. The consistency between the libcbm and CBM-CFS3 
was checked by running exactly the same assumptions (i.e. same Archive Index Database, or aidb for the 
respective country) and datasets for the historical period (i.e. from the available initial year reported as the 
inventory year until 2015) for all 25 countries in the EU cbm-cfs3 database.  
The percentage difference between results by each model was checked for the initialized stocks (i.e. time step 
0) and the stocks achieved during the simulation (i.e. time step 15) for the 25 countries as Member States of 
the EU. Checks were done using the estimates aggregated country scale.  
For the time step 0, there was no difference among the countries for the initialized stocks for any carbon 
pool.    
For time step 15, there were no differences for 11 countries. Consequently, we can safely appreciate that the 
two models provide for fully consistent results. For the remaining 14 countries, there were differences as

## Стр. 44

41 
shown in Table A1. Apparently, such differences exist because the simulation assumptions include natural 
disturbances which are randomly allocated by the models, so they result in slightly different values of the 
carbon stocks for each model. Differences are larger dead organic matter pools than for living biomass, while 
they are larger for small pools (e.g. snags) than for large pools (merchantable, soil organic matter).  
Table A1. Maximal deviation of libcbm vs. cbm-cfs3 carbon pools in the time step 15 across the 25 member 
states compared (in %, rounded to 0.5pp). 
Carbon pools 
libcbm/cbm-cfs3 carbon pools 
Deviation (%) 
Living biomass pools 
softwood_coarse_roots 
±3.5 
softwood_foliage 
±3 
softwood_merch 
±3 
softwood_other 
±3 
hardwood_foliage 
±1 
hardwood_merch 
±1 
hardwood_coarse_roots 
±1 
hardwood_other 
±1 
softwood_fine_roots 
±1 
hardwood_fine_roots 
±1 
Dead organic matter 
pools 
softwood_stem_snag 
±14 
softwood_branch_snag 
±11 
above_ground_fast_soil 
±3 
below_ground_fast_soil 
±2 
hardwood_branch_snag 
±2 
hardwood_stem_snag 
±2 
medium_soil 
±1 
above_ground_very_fast_soil 
±1 
below_ground_very_fast_soil 
±1 
above_ground_slow_soil 
±1 
below_ground_slow_soil 
±0 
low_ground_very_fast_soil 
±0 
above_ground_very_fast_soil 
±0.5

*Таблица 44.1:*

| Carbon pools | libcbm/cbm-cfs3 carbon pools | Deviation (%) |
|---|---|---|
| Living biomass pools | softwood_coarse_roots | ±3.5 |
|  | softwood_foliage | ±3 |
|  | softwood_merch | ±3 |
|  | softwood_other | ±3 |
|  | hardwood_foliage | ±1 |
|  | hardwood_merch | ±1 |
|  | hardwood_coarse_roots | ±1 |
|  | hardwood_other | ±1 |
|  | softwood_fine_roots | ±1 |
|  | hardwood_fine_roots | ±1 |
| Dead organic matter pools | softwood_stem_snag | ±14 |
|  | softwood_branch_snag | ±11 |
|  | above_ground_fast_soil | ±3 |
|  | below_ground_fast_soil | ±2 |
|  | hardwood_branch_snag | ±2 |
|  | hardwood_stem_snag | ±2 |
|  | medium_soil | ±1 |
|  | above_ground_very_fast_soil | ±1 |
|  | below_ground_very_fast_soil | ±1 |
|  | above_ground_slow_soil | ±1 |
|  | below_ground_slow_soil | ±0 |
|  | low_ground_very_fast_soil | ±0 |
|  | above_ground_very_fast_soil | ±0.5 |

## Стр. 45

 
 
 
 
GETTING IN TOUCH WITH THE EU 
In person 
All over the European Union there are hundreds of Europe Direct centres. You can find the address of the centre nearest you online 
(european-union.europa.eu/contact-eu/meet-us_en). 
On the phone or in writing 
Europe Direct is a service that answers your questions about the European Union. You can contact this service: 
— by freephone: 00 800 6 7 8 9 10 11 (certain operators may charge for these calls), 
— at the following standard number: +32 22999696, 
— via the following form: european-union.europa.eu/contact-eu/write-us_en. 
 
FINDING INFORMATION ABOUT THE EU 
Online 
Information about the European Union in all the official languages of the EU is available on the Europa website (european-
union.europa.eu). 
EU publications 
You can view or order EU publications at op.europa.eu/en/publications. Multiple copies of free publications can be obtained by 
contacting Europe Direct or your local documentation centre (european-union.europa.eu/contact-eu/meet-us_en). 
EU law and related documents 
For access to legal information from the EU, including all EU law since 1951 in all the official language versions, go to EUR-Lex 
(eur-lex.europa.eu). 
Open data from the EU 
The portal data.europa.eu provides access to open datasets from the EU institutions, bodies and agencies. These can be 
downloaded and reused for free, for both commercial and non-commercial purposes. The portal also provides access to a wealth 
of datasets from European countries.

## Стр. 46


*Таблица 46.1:*

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
