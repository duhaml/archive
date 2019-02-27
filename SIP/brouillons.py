from matplotlib import pyplot as plt
import numpy as np

def gender_city_happiness():
    city=['Delhi','Beijing','Washington','Tokyo','Moscow']
    Gender=['Male','Female']
    pos = np.arange(len(city))
    bar_width = 0.35
    Happiness_Index_Male=[60,40,70,65,85]
    Happiness_Index_Female=[30,60,70,55,75]
    plt.bar(pos, Happiness_Index_Male, bar_width, color='blue', edgecolor='black')
    plt.bar(pos+bar_width, Happiness_Index_Female, bar_width, color='pink', edgecolor='black')
    plt.xticks(pos+bar_width/2, city)
    plt.xlabel('City', fontsize=16)
    plt.ylabel('Happiness Index', fontsize=16)
    plt.title('Group Barchart - Happiness index across cities By Gender',fontsize=18)
    plt.legend(Gender,loc=2)
    plt.show()

def center_axes(fig):
    ax = plt.figure().add_subplot(1, 1, 1)
    # Move left y-axis and bottom x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

def plot_parabola():
    x = np.linspace(-2,2,200) # 200 linearly spaced numbers
    y = x**2
    center_axes(plt)
    plt.plot(x,y)
    plt.show()

import math

def plot_sine():
    x = np.linspace(-2, 2, 200)
    y1 = np.sin(math.pi * x)
    y2 = np.sin(2 * math.pi * x)
    center_axes(plt)
    plt.plot(x, y1, x, y2)
    plt.show()

def plot_sine_simp():
    x = [-2+i/50 for i in range(201)]
    y1 = [math.sin(math.pi * i) for i in x]
    y2 = [math.sin(2 * math.pi * i) for i in x]
    center_axes(plt)
    plt.plot(x, y1, x, y2)
    plt.show()

def two_figures():
    x = np.linspace(-2,2,200)
    plt.subplot(211)
    plt.plot(x, np.sin(math.pi * x), 'rv')
    plt.subplot(212)
    plt.plot(x, np.sin(2 * math.pi * x), 'b+')
    plt.show()


###############   about pi    #######""

# The red square without using numpy
def red_square(n) :
    img = [[(128,29,59) for i in range(n)] for j in range(n)]
    plt.imshow(img)
    plt.show()

# Other way if pyplot complains about data types
# uint8 = unigned integer coded on 8 bits (0..255)
def red_square_uint(n) :
    img = [[(128,29,59) for i in range(n)] for j in range(n)]
    plt.imshow(np.asanyarray(img, dtype='uint8'))
    plt.show()

def deep_red_square(n):
    img = np.zeros((n, n, 3), dtype='uint8') # you could also use a list of list of list.
    for i in range(n):
        for j in range(n):
            img[i][j] = [128,29,58]
    imgplot = plt.imshow(img)
    plt.axis('off')
    plt.show()


colors = [
    [230, 230, 230],   # white
    [255,  65,  54],   # red
    [255,  53,  27],   # orange
    [255, 220,   0],   # yellow
    [1,   255, 112],   # light green
    [61,  153, 112],   # dark green
    [57,  204, 204],   # light blue
    [0,   116, 217],   # dark blue
    [177,  13, 201],   # purple
    [240,  18, 190]    # pink
]

def color_square_digits(dig, n):
    img=[[[0,0,0] for i in range(n)] for j in range(n)]
    i = 0
    j = 0
    for k in range(len(dig)):
        img[i][j] = colors[int(dig[k])]
        j = (j + 1) % n
        if j == 0:
            i = (i + 1) % n
            if i == 0 :
                break
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def frac(a, b, n) :
    """
    return the n first digits of the fractional part of a/b
    """
    digits = ""
    for d in range(n) :
        a *= 10
        digits += str((a // b) % 10)
    return digits

big_pi = """\
31415926535897932384626433832795028841971693993751058209749445923078164062862\
089986280348253421170679821480865132823066470938446095505822317253594081284811\
174502841027019385211055596446229489549303819644288109756659334461284756482337\
867831652712019091456485669234603486104543266482133936072602491412737245870066\
063155881748815209209628292540917153643678925903600113305305488204665213841469\
519415116094330572703657595919530921861173819326117931051185480744623799627495\
673518857527248912279381830119491298336733624406566430860213949463952247371907\
021798609437027705392171762931767523846748184676694051320005681271452635608277\
857713427577896091736371787214684409012249534301465495853710507922796892589235\
420199561121290219608640344181598136297747713099605187072113499999983729780499\
510597317328160963185950244594553469083026425223082533446850352619311881710100\
031378387528865875332083814206171776691473035982534904287554687311595628638823\
537875937519577818577805321712268066130019278766111959092164201989380952572010\
654858632788659361533818279682303019520353018529689957736225994138912497217752\
834791315155748572424541506959508295331168617278558890750983817546374649393192\
550604009277016711390098488240128583616035637076601047101819429555961989467678\
374494482553797747268471040475346462080466842590694912933136770289891521047521\
620569660240580381501935112533824300355876402474964732639141992726042699227967\
823547816360093417216412199245863150302861829745557067498385054945885869269956\
909272107975093029553211653449872027559602364806654991198818347977535663698074\
265425278625518184175746728909777727938000816470600161452491921732172147723501\
414419735685481613611573525521334757418494684385233239073941433345477624168625\
189835694855620992192221842725502542568876717904946016534668049886272327917860\
857843838279679766814541009538837863609506800642251252051173929848960841284886\
269456042419652850222106611863067442786220391949450471237137869609563643719172\
"""

# color_square_digits(frac(1,17,40*40), 40)
# color_square_digits(big_pi, 40)


import matplotlib.patches as patches


def approx_pi(n) :
    inside = 0
    total = 0
    while total < n :
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        total += 1
        if math.hypot(x, y) < 1 :
            inside += 1
    almost_pi = 4 * (inside / total)
    rel_error = math.fabs(almost_pi - math.pi) / math.pi
    return (almost_pi, rel_error)

# approx_pi(1000)
# approx_pi(100000)

def plot_monte_carlo() :
    fig = plt.figure()         # Create a figure
    fig.patch.set_facecolor('white') # Set its background to white
    axes = plt.axes()          # Create the axes of the figure
    axes.set_aspect('equal')   # Set their aspect ratio to 1
    axes.set_axis_off()        # Do not display the axes
    axes.set_xlim(left=-1, right=1.1)  # The .1 is for avoiding to clip the rectangle
    axes.set_ylim(bottom=-1.1, top=1)
    # Add the rectangle and the circle
    axes.add_patch(patches.Circle((0, 0), 1, linewidth=1, fill=False, edgecolor='blue'))
    axes.add_patch(patches.Rectangle((-1, -1), 2, 2, linewidth=1, fill=False))

def approx_pi_plot(n) :
    plot_monte_carlo()
    inside = 0
    total = 0
    while total < n :
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        total += 1
        if math.hypot(x, y) < 1 :
            inside += 1
            plt.plot(x, y, 'ro', markersize=2)
        else:
            plt.plot(x, y, 'go', markersize=2)
        plt.pause(0.05)  # Pause for animation
    plt.show()
    almost_pi = 4 * (inside / total)
    rel_error = math.fabs(almost_pi - math.pi) / math.pi
    return (almost_pi, rel_error)

############## Koch snowflake  #########

import cmath  # complex numbers

def iso_triangle() :
    a = complex(0,0)
    b = complex(1,0)
    ac = (b-a) * cmath.rect(1, math.pi/3)
    c = a + ac
    return ([a.real, c.real, b.real, a.real],
            [a.imag, c.imag, b.imag, a.imag])

# plt.axes().set_aspect('equal')
# isot = iso_triangle()
# plt.plot(isot[0], isot[1])

def koch_seg(segx, segy, pos = 0) :
    # We use complex numbers to represent points
    a = complex(segx[pos], segy[pos])         # get point A
    b = complex(segx[pos + 1], segy[pos + 1]) # and point B
    ab = b - a      # Compute vector AB
    ac = ab / 3     # Cut the segment at 1/3 of its length
    c = a + ac      # to find point C
    # The next point is at 1/3 of AB, turned by 60° (pi/3), relative to C
    cd = ac * cmath.rect(1, math.pi/3)  # Can also be written ac * complex(math.cos(math.pi/3), math.sin(math.pi/3))
    d = c + cd
    # The last point is at 2/3 of AB
    ae = 2 * ab / 3
    e = a + ae
    return ([a.real, c.real, d.real, e.real, b.real],
            [a.imag, c.imag, d.imag, e.imag, b.imag])

def koch_iter(segsx, segsy) :
    finalx = []
    finaly = []
    for pos in range(len(segsx) - 1) :
        nsegs = koch_seg(segsx, segsy, pos)
        finalx = finalx + nsegs[0]
        finaly = finaly + nsegs[1]
    return (finalx, finaly)

def vonKoch(n) :
    k = iso_triangle()
    for i in range(n) :
        k = koch_iter(k[0], k[1])
    plt.axes().set_aspect('equal')
    plt.plot(k[0], k[1])
    plt.show()


############# pendu ###########

import random

def raw_version() :
    AA = ("python", "information", "systems", "programming", "centralesupelec")
    a = random.choice(AA)
    b = ''
    c = 10
    while c > 0:
        d = 0
        for e in a:
            if e in b:
                print(e)
            else:
                print("*")
                d += 1
        if d == 0:
            print("You won")
            break
        f = input("guess a character:")
        b += f
        if f not in a:
            c -= 1
            print("Wrong, you have ", + c, "more guesses")
            if c == 0:
                print("You Lost, the word was: " + a)

def clean_version() :
    words = ("python", "information", "systems", "programming", "centralesupelec")
    word = random.choice(words)
    guessed = ''
    rem_turns = 10
    while rem_turns > 0:
        nb_missing = 0
        for letter in word:
            if letter in guessed:
                print(letter)
            else:
                print("*")
                nb_missing += 1
        if nb_missing == 0:
            print("You won")
            break
        guess = input("guess a character:")
        if guess not in word:
            rem_turns -= 1
            if rem_turns == 0:
                print("Wrong guess, you lose, the word was: " + word)
            else:
                print("Wrong, you have ", + rem_turns, "more guesses")
        else :
            guessed += guess

# Structured version
def print_check(word, guessed) :
    wins = True
    for letter in word:
        if letter in guessed:
            print(letter)
        else:
            print("*")
            wins = False
    return wins

def check_guess(guess, word, turns) :
    good_guess = True
    if guess not in word :
        turns -= 1
        good_guess = False
        if turns == 0:
            print("Wrong guess, you lose, the word was: " + word)
        else:
            print("Wrong, you have ", + turns, "more guesses")
    return (good_guess, turns)

def simple_game(word, turns) :
    guessed = ''
    rem_turns = turns
    while rem_turns > 0:
        if print_check(word, guessed) :
            print("You win!")
            break
        guess = input("guess a character:")
        (good_guess, rem_turns) = check_guess(guess, word, rem_turns)
        if good_guess:
            guessed += guess

# simple_game(random.choice(("python", "information", "systems", "programming", "centralesupelec")), 9)

# Full version

def get_guessed_word(secret_word, letters_guessed):
    masked_word = ""
    for l in secret_word :
        if l in letters_guessed :
            masked_word += l
        else:
            masked_word += '*'
    return masked_word

def check_guessed_word(secret_word, letters_guessed) :
    return "*" not in get_guessed_word(secret_word, letters_guessed)


def word_game(secret_word, max_guesses) :
    letters_guessed = ''
    available_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    num_guesses = 0
    while not check_guessed_word(secret_word, letters_guessed) \
      and num_guesses < max_guesses :
        print(max_guesses - num_guesses, " guesses left")
        print("available letters: ", available_letters)
#        guess = input("Your guess: ")
        guess = validate_input(input("Your guess: "))
        num_guesses += 1
        if guess in available_letters :
            available_letters.remove(guess)
            if guess in secret_word :
                letters_guessed += guess
                print("Good: ", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Sorry: ", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Be careful, just just wasted a guess on an already tested letter!")

    if check_guessed_word(secret_word, letters_guessed) :
        return num_guesses
    else:
        return -1


def calc_max_guesses(secret_word) :
    # Allow two guesses for each distinct letter
    return len(set(secret_word)) * 2

scrabble_values = {
    'a': 1, 'b': 3,'c': 3, 'd': 2, 'e': 1,'f': 4,'g': 2,'h': 4,'i': 1,
    'j': 8,'k': 5,'l': 1,'m': 3,'n': 1,'o': 1,'p': 3,'q': 10,'r': 1,'s': 1,
    't': 1,'u': 1,'v': 4,'w': 4,'x': 8,'y': 4, 'z': 10
}

def calc_score(secret_word, num_guesses, letter_values = scrabble_values) :
    score = 0
    for l in set(secret_word):
        score += letter_values[l]
    score += calc_max_guesses(secret_word) - num_guesses
    return score


def real_word_game(secret_word) :
    n = word_game(secret_word, calc_max_guesses(secret_word))
    if n < 0 :
        print("You lose.")
    else:
        print("You win with score: ", calc_score(secret_word, n))

def validate_input(l) :
    if l.isalpha() :
        return l
    else:
        return validate_input(input("# Invalid input, please type only letters: "))


def guess_whole_word(secret_word):
    guess = validate_input(input("guess a word: "))
    if guess == secret_word :
        return 0 # As if guessed in no turn
    else:
        return -1

def word_game_w(secret_word, max_guesses) :
    letters_guessed = ''
    available_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    num_guesses = 0
    while not check_guessed_word(secret_word, letters_guessed) \
      and num_guesses < max_guesses :
        print(max_guesses - num_guesses, " guesses left")
        print("available letters: ", available_letters)
        guess = input("Your guess, or * for guessing the whole word: ")
        if guess == "*":
            return guess_whole_word(secret_word)
        guess = validate_input(guess)
        num_guesses += 1
        if guess in available_letters :
            available_letters.remove(guess)
            if guess in secret_word :
                letters_guessed += guess
                print("Good: ", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Sorry: ", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Be careful, just just wasted a guess on an already tested letter!")

    if check_guessed_word(secret_word, letters_guessed) :
        return num_guesses
    else:
        return -1

def real_word_game_w(secret_word) :
    n = word_game_w(secret_word, calc_max_guesses(secret_word))
    if n < 0 :
        print("You lose.")
    else:
        print("You win with score: ", calc_score(secret_word, n))


def random_word_game(secret_word, max_guesses) :
    letters_guessed = ''
    available_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    num_guesses = 0
    while not check_guessed_word(secret_word, letters_guessed) \
      and num_guesses < max_guesses :
        print(max_guesses - num_guesses, " guesses left")
        print("available letters: ", available_letters)
        guess = random.choice(available_letters)
        num_guesses += 1
        available_letters.remove(guess)
        if guess in secret_word :
            letters_guessed += guess
            print(guess, " is good: ", get_guessed_word(secret_word, letters_guessed))
        else:
            print(guess, " is not in the word: ", get_guessed_word(secret_word, letters_guessed))

    if check_guessed_word(secret_word, letters_guessed) :
        return num_guesses
    else:
        return -1


def match(word, guess_pattern, letters_tried):
    """
    Check if a word is a possible solution according to the guess pattern
    and the letters that have already been tried.
    :param word: the word to test
    :param guess_pattern: the guess pattern, which is the secret word with '*' in place of not yet guessed letters
    :param letters_tried: the letters that have already been tried to guess the secret word
    :return: True if the word can be the secret word, else False
    """
    if len(word) != len(guess_pattern) :
        # If the word does not have the right length, we can reject it
        return False
    for i in range(len(guess_pattern)) :
        # Check if the word matches the current guess (with '*' in place of not yet guessed characters)
        if guess_pattern[i] != "*" and guess_pattern[i] != word[i] :
            return False
        # Ignore words that contains already tried letters which are not in the pattern
        if not word[i] in guess_pattern and word[i] in letters_tried :
            return False
    return True

def probabilities(guess_pattern, letters_tried, dic):
    # Filter out words that cannot be the secret one
    possible_words = [word for word in dic if match(word, guess_pattern, letters_tried)]
    print("# possibilities for ", guess_pattern, ": ", possible_words)
    # Count the number of occurrences of a character
    frequencies = {}
    for word in possible_words :
        for c in word :
            if c in letters_tried :
                # Ignore already characters that have already been tried
                continue
            if c in frequencies :
                frequencies[c] += 1
            else:
                frequencies[c] = 1
    print("# freq for ", guess_pattern, ": ", frequencies)
    # Get the total number of distinct characters
    total_chars = sum(frequencies.values())
    # Fill the table of probabilities
    prob = {}
    for c in frequencies.keys() :
        prob[c] = frequencies[c] / total_chars
    return prob

def ai_word_game(secret_word):
    with open("../dic.txt", "r") as dict_file :
        words = dict_file.read().lower().splitlines()
        dic = [word.replace("-", "").replace("-", "") for word in words]
    letters_tried = ''
    num_guesses = 0
    max_guesses = calc_max_guesses(secret_word)

    while num_guesses < max_guesses \
      and not check_guessed_word(secret_word, letters_tried) :
        probs = probabilities(get_guessed_word(secret_word, letters_tried), letters_tried, dic)
        guess = max(probs, key=probs.get)
        num_guesses += 1
        letters_tried += guess
        if guess in secret_word :
            print(guess, " is good: ", get_guessed_word(secret_word, letters_tried))
        else:
            print(guess, " is not in the word: ", get_guessed_word(secret_word, letters_tried))

    if check_guessed_word(secret_word, letters_tried) :
        print("AI wins with score: ", calc_score(secret_word, num_guesses))
    else:
        print("AI loses.")



###############################  Mandelbrot sets   #######

def module_real_img(z) :
    return math.hypot(z.real, z.imag)

def module_conj(z) :
    return math.sqrt((z.conjugate()*z).real)

def mandelfunc(c, z) :
    return z*z + c

def mandelbrot(c, n_max) :
    z = 0
    n = 0
    while n < n_max and abs(z) < 2 :
        n += 1
        z = mandelfunc(c, z)
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, xnum, ynum, n_max) :
    x = [xmin + i * (xmax - xmin)/xnum for i in range(xnum+1)]
    y = [ymin + i * (ymax - ymin)/ynum for i in range(ynum+1)]
    z = [[mandelbrot(complex(x[i], y[j]), n_max) for i in range(xnum)] for j in range(ynum)]
    return z

def plot_mandelbrot(xmin, xmax, ymin, ymax, xnum, ynum, n_max) :
    z = mandelbrot_set(xmin, xmax, ymin, ymax, xnum, ynum, n_max)
    mycolors = [(1,0,0), (0,1,0), (0,0,1), (0,0,0)]
    colmap = colors.LinearSegmentedColormap.from_list("mandelbrot", mycolors, 16)
    plt.imshow(z, cmap=colmap, interpolation='bicubic')
    plt.show()

# plot_mandelbrot(-2.25, 0.75, -1.25, 1.25, 1500, 1250, 64)



##
# PageRank
##
def subdiv_one(n):
    elems = [random.random() for _  in range(n)]
    norm = sum(elems)
    return [elem / norm for elem in elems]

import numpy as np
def create_transition_matrix(size) :
    # First, we create a matrix whose lines sum up to 1
    m = np.matrix([subdiv_one(size) for i in range(size)])
    # and we transpose it to have columns that sum up to 1
    return m.transpose()

# https://en.wikipedia.org/wiki/Matrix_norm
import numpy.linalg as la

def page_rank(size, epsilon) :
    m = create_transition_matrix(size)
    s0 = [[1/size] for _ in range(size)]  # 1 column matrix
    rank = 0
    norm = la.norm((m ** (rank + 1) - m ** rank), np.inf)
    while (norm/size > epsilon) :
        rank += 1
        norm = la.norm((m ** (rank + 1) - m ** rank), np.inf)
    return (m ** rank) * s0

# More efficient version, which does not recompute m**k at
# each iteration. It also compare the norm directly to epsilon,
# without dividing by the number of pages
def page_rank_lowcost(size, epsilon) :
    m = create_transition_matrix(size)
    mk = m
    s0 = [[1/size] for _ in range(size)]
    rank = 0
    norm = la.norm(m, np.inf)
    while (norm > epsilon) :
        rank += 1
        mk2 = mk * m
        norm = la.norm((mk2 - mk), np.inf)
        mk = mk2
    return mk * s0


############ Prey-predator system #######""

# The function that gives the derivative from the current values
def f(x, y, a, b) :
    return x * (a - b * y)

# The function that gives the next value of z (which is either x or y)
# from the current value of z, of the other variable (t), the parameters
# of the problem (a and b) and the integration step (Euler explicit scheme).
def next_step(zn, tn, a, b, step) :
    return zn + step * f(zn, tn, a, b)

def populations(x0, y0, alpha, beta, delta, gamma, step, n) :
    x, y = x0, y0
    lx, ly = [x0], [y0]
    for _ in range(n) :
        # We have dx/dt =  alpha*x - beta*x*y
        # and     dy/dt = -gamma*y + delta*y*x
        # hence the parameters of next_step
        x, y = next_step(x, y, alpha, beta, step), \
               next_step(y, x, -gamma, -delta, step)
        lx.append(x)
        ly.append(y)
    return lx, ly

def display_populations() :
    # Initial populations
    x0, y0 = 0.9, 0.9
    # Parameters
    alpha, beta, delta, gamma = 2/3, 4/3, 1, 1
    # Temporal resolution
    resolution = 1000
    # Compute until that time
    time_max = 20
    # Time step size
    step = 1 / resolution
    # Total number of steps
    n = time_max * resolution
    ## Compute the populations
    prey, pred = populations(x0, y0, alpha, beta, delta, gamma, step, n)
    # Plot the result
    time = [step * i for i in range(n+1)]
    plt.subplot(121)
    # First subplot for the evolution of populations through time
    plt.title("Population versus time")
    plt.plot(time, prey, label="Preys")
    plt.plot(time, pred, label="Predators")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.legend(loc='upper left')
    # Second subplot for the phase diagram
    plt.subplot(122)
    plt.title("Predators versus preys")
    plt.plot(prey, pred)
    plt.xlabel("Preys")
    plt.ylabel("Predators")
    plt.show()
