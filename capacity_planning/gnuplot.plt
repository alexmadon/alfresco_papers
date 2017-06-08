set terminal png
set output 'out.png'
set datafile separator ","
plot  "output.txt" using 1:2 title 'alf_data', "output.txt" using 1:3 title 'indexes'


