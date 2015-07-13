timepaster
====================

A very simple command line time card calculator to get the decimal difference
between hh:mm-hh:mm. The basis of the code was copied a long time ago from a
page I cannot find anymore, so I cannot cite the original author (I would like
to, though).

This is typically something you can use if you have to fill in time sheets or
time tracking software. On the commandline you would do the following:

    $ timepaster
    $ Enter Start-End (hh:mm-hh:mm): 09.36-11.18 

and the result is displayed as:

               Duration: 1 hrs and 42 min
               Decimal difference: 1.7
               ______________________________


**The decimal time difference is also loaded into the clipboard**. So now you can
just "paste" (ctrl-v) from your system clipboard and the calculated value
will appear.

The time notation with points is simply because 09.36 is faster to type
on a numpad than 09:36.

Type "quit" to exit the commandline app.

**TODO:**
- Use copied time calculatoin strings as input  (copy: 12.36-16.42 and place the 
  result in the clipboard)
- Accept different time formats (as long as they are consistent) such as 
  01.36, 01:36, 1:36.

