import sys

def num_atack(n, k, c_q, r_q, obstacles) :

    d11 = min( c_q-1, r_q-1 )
    d12 = min( n-c_q, n-r_q )
    d21 = min( n-c_q, r_q-1 )
    d22 = min( c_q-1, n-r_q )

    r1 = r_q-1
    r2 = n-r_q
    c1 = c_q-1
    c2 = n-c_q

    for i in range(k):
        if ( c_q > obstacles[i][0] and r_q > obstacles[i][1] and c_q-obstacles[i][0] == r_q-obstacles[i][1] ) :
            d11 = min(d11, c_q-obstacles[i][0]-1) 

        if ( obstacles[i][0] > c_q and obstacles[i][1] > r_q and obstacles[i][0]-c_q == obstacles[i][1]-r_q ) :
            d12 = min( d12, obstacles[i][0]-c_q-1)

        if ( obstacles[i][0] > c_q and r_q > obstacles[i][1] and obstacles[i][0]-c_q == r_q-obstacles[i][1] ) :
            d21 = min(d21, obstacles[i][0]-c_q-1)

        if ( c_q > obstacles[i][0] and obstacles[i][1] > r_q and c_q-obstacles[i][0] == obstacles[i][1]-r_q ) :
            d22 = min(d22, c_q-obstacles[i][0]-1)

        if ( c_q == obstacles[i][0] and obstacles[i][1] < r_q ) :
            r1 = min(r1, r_q-obstacles[i][1]-1)

        if ( c_q == obstacles[i][0] and obstacles[i][1] > r_q ) :
            r2 = min(r2, obstacles[i][1]-r_q-1)

        if ( r_q == obstacles[i][1] and obstacles[i][0] < c_q ) :
            c1 = min(c1, c_q-obstacles[i][0]-1)

        if ( r_q == obstacles[i][1] and obstacles[i][0] > c_q ) :
            c2 = min(c2, obstacles[i][0]-c_q-1)

    return d11 + d12 + d21 + d22 + r1 + r2 + c1 + c2


data = []
obstacles = []

with open('data.txt') as fileobj:
    for line in fileobj:
        line = line.split(" ")
        line[0] = int(line[0])
        line[1] = int(line[1].strip())
        data.append(line)
n = data[0][0]
k = data[0][1]
r_q = data[1][0]
c_q = data[1][1]
obstacles = data[2:]

try:
    if (n <= 0 or n >= 10^5):
        raise ValueError("Error! No se permite ese rango")
except ValueError:
        print("Error! No se permite ese rango")
        sys.exit(1)

try:
    if (k < 0 or k >= 10^5):
        raise ValueError("Error! No se permite ese numero de obstaculos")
except ValueError:
        print("Error! No se permite ese numero de obstaculos")
        sys.exit(1)

for item in obstacles:
    try:
        if (item[0] == r_q and item[1] == c_q):
            raise ValueError("Error! Un obstaculo no puede tener la misma posición de la reina")
    except ValueError:
            print("Error! Un obstaculo no puede tener la misma posición de la reina")
            sys.exit(1)

print(num_atack(n, k, r_q, c_q, obstacles))


# 0 < n <= 10^5
# 0 <= k <= 10^5
# A single cell may contain more than one obstacle
# There will never be an obstacle at the position where the queen is located