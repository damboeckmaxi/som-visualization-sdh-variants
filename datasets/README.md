Provide your datasets here! Use The SOMLib file format(http://www.ifs.tuwien.ac.at/dm/somtoolbox/somlibFileFormat.html)
One dataset consists of(Template-vector file pairs can also contain multiple property-files):
* .tv - template-file
* .vec - Vector-file
* .prop - Property file that contains training-spec for the som

The Following requirements have to be made for the .prop-file:
* outputDirectory=../maps/<prop-file-name>
* namePrefix=<prop-file-name>
* vectorFileName=../datasets/<vec-name>
* templateFileName=../datasets/<tv-name>

while <prop-file-name> is the name of the property file without the .prop-ending.
A few example-datasets are provided.(from http://www.ifs.tuwien.ac.at/dm/somtoolbox/datasets.html)