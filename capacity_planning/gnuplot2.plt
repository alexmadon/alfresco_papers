set terminal png
set output 'out2.png'
set datafile separator ","
plot  "output.txt" using 1:($3/$2) title 'ratio'


