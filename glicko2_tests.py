"""
Copyright (c) 2009 Ryan Kirkman

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import glicko2
import timeit


def exampleCase():
    # Create a player called Ryan
    Ryan = glicko2.Player("Ryan")
    p1 = glicko2.Player("p1")
    p1.rating = 1300
    p1.rd = 50
    p2 = glicko2.Player("p2")
    p2.rating = 2000
    p2.rd = 500
    p3 = glicko2.Player("p3")
    p3.rating = 1900
    p3.rd = 300
    Ryan.addMatch(p1, 0)
    Ryan.addMatch(p2, 1)
    Ryan.addMatch(p2, 0)
    Ryan.addMatch(p3, 0)

    # Following the example at:
    # http://math.bu.edu/people/mg/glicko/glicko2.doc/example.html
    # Pretend Ryan (of rating 1500 and rating deviation 350)
    # plays players of ratings 1400, 1550 and 1700
    # and rating deviations 30, 100 and 300 respectively
    # with outcomes 1, 0 and 0.
    print("Old Rating: " + str(Ryan.rating))
    print("Old Rating Deviation: " + str(Ryan.rd))
    print("Old Volatility: " + str(Ryan.vol))
    Ryan.update_player()
    print("New Rating: " + str(Ryan.rating))
    print("New Rating Deviation: " + str(Ryan.rd))
    print("New Volatility: " + str(Ryan.vol))
   # Ryan.addMatch(p2, 1)
    Ryan.update_player()
    Ryan.did_not_compete()
    print("New Rating: " + str(Ryan.rating))
    print("New Rating Deviation: " + str(Ryan.rd))
    print("New Volatility: " + str(Ryan.vol))

if __name__ == "__main__":
    exampleCase()

