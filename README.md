This is a re-typed version of the first program that I ever sold. Around the age
of 14 my dad asked me if I could write a program that would calculate group
insurance quotes for him. The process consisted of gathering information about
all of the employees in a small company (he usually targeted companies with less
than 50 employees.) For each employee he needed to lookup a rate from a table
rows corresponding to age groups (< 29, 30-34, 35-39, etc.) The columns were
Male, Female, and Dependent. So, for a male, age 37, with dependent coverage he
needed to find the row for ages 35-39, then go to the column for males and write
down that cost. Then moving over to the "dependent" column, write down that
cost. He would repeat this for each employee in the company and then total them
all up and the result would be the company cost for health insurance. This was
obviously tedious and error prone, especially if you remember that this was
before spreadsheets so it was all a manual process. On top of this, he often
quoted rates from two or more carriers for each company, to give them choices
for coverage and costs.

I had only written a few basic "demo" programs at this point, "Guess the Number"
type games. But the Apple ][+ computer came with all of the manuals for learning
BASIC and simple computer programming. I had taught myself a little bit but I
started digging into it more and wrote this program. He paid me something for it
which was nice, but then he showed it to a friend who was in the same business
and his friend said, "I'd pay money for that!" and gave me $500.

Altogether that summer I made about $2,000 (in 1981 dollars, so about $6,000
today.) This blew my mind. The idea that I could make money for something that I
created on the computer, and not only that, that I could continue to make money
from it even after the first sale, was life changing for me.

Over the next year or two I made other versions of it for other companies. At
one point I was asked by a small insurance company with a couple of dozen agents
to create a version for them that ran on the IBM PC and they promised they would
be a copy for each of their agents. I had recently acquired a copy of Borland's
Turbo Pascal and taught myself Pascal so I could write it in that. I discovered
a technique for writing directly to video memory, to bypass the BIOS (which was
extremely slow) and created a text based menuing system. I worked on it until it
was quite polished (at least for a high school student.) About the time I was
ready to deliver it the owner decided to pay his son to write a similar program
instead. The person who had asked me to write it for them felt really bad and
paid me $250 but it was a big disappointment still.

Anyway, I've had this printout for around 40 years now. The source code for all
versions has been lost long ago. Since it was so instrumental in forming my
early desires for computers I decided to try OCR to scan it into source form
again. It did about 70% and then I spent a few hours correcting the mistakes. It
is runnable now in an Apple ][ emulator but it is missing the RATE file which
basically duplicated the tables that the carriers published. It's format was
simple, 9 numbers to specify the cost for males, one for each age category,
followed by 9 numbers for females, followed by a final 9 for dependent costs.
Finally there were two more numbers for "Dental for employees", "Dental for
dependents" respectively.

This is just for posterity, it has no practical use at this point.
