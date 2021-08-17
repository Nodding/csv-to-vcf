# csv-to-vcf
Takes a file named "input.csv" formatted in a certain manner and converts it to "output.vcf"

Refer to the example csv to see how to format your contacts.
  You will need the columns Name, Cell, Work and Home.
  Be sure to deliminate numbers by dashes (-).
  I'd also make sure all your data has white space removed on both ends.
  

The input.csv must be in the same directory as the python script. The output.vcf is placed in the same directory.

This uses Python 2.7.18, and generates vcfs in version 2.1.
