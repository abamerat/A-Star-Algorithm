from random import randint
def distance(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return max(abs(x1 - x2), abs(y1 - y2))


def adj(cell):
    x, y = cell
    nums = (-1,0,1)
    adjCells = []
    for dx in nums:
            for dy in nums:
                if (dx, dy) != (0, 0):
                    adjCells.append((x + dx, y + dy))
    return adjCells


def createCell(position, status, target):
    cellDistance = distance(position, target)
    return {
        "Status": status,
        "f": cellDistance,
        "g": 1000,
        "h": cellDistance,
        "key": position,
        "parent": None
    }


tPos = (randint(-9, 9), randint(-9, 9))

closedCells = {}
openCells = {}

sNode = createCell((0, 0), "Start", tPos)

sNode["g"] = 0
sNode["f"] = sNode["g"] + sNode["h"]

openCells[sNode["key"]] = sNode

nodes = 0

print("Target:", tPos)


while nodes < 100000:

    for i in adj(sNode["key"]):

        if i in closedCells:
            continue

        newG = sNode["g"] + 1

        if i in openCells:

            cell = openCells[i]

            if newG < cell["g"]:
                cell["g"] = newG
                cell["f"] = newG + cell["h"]
                cell["parent"] = sNode["key"]

        else:

            if i == tPos:
                status = "Target"
            else:
                status = "Open"

            cell = createCell(i, status, tPos)

            cell["g"] = newG
            cell["f"] = cell["g"] + cell["h"]
            cell["parent"] = sNode["key"]

            openCells[i] = cell


    lowestnode = None

    for i, cell in openCells.items():
        if lowestnode is None or cell["f"] < lowestnode["f"]:
            lowestnode = cell
    if lowestnode is None:
        print("No path!")
        break

    del openCells[lowestnode["key"]]
    closedCells[lowestnode["key"]] = lowestnode
    sNode = lowestnode
    nodes += 1
    print(lowestnode["key"],"f:", lowestnode["f"],"g:", lowestnode["g"])
    if lowestnode["Status"] == "Target":

        print("\nTarget found!")
        print("Nodes searched:", nodes)
        print("Path length:", lowestnode["g"])       
        path = []
        cnode = lowestnode

        while cnode is not None:
            path.append(cnode)
            if cnode["parent"] is None:
                break
            cnode = closedCells[cnode["parent"]]
        path.reverse()
        print("Path:")
        for i, pathCell in enumerate(path):
            print(i, pathCell["key"])
        print("")
        print("Done!")
        break