def Matching(x, y):
    if x==0 and y==0:
        return '1A'
    elif x==1 and y==0:
        return '1B'
    elif x==2 and y==0:
        return '1C'
    elif x==3 and y==0:
        return '1D'
    elif x==4 and y==0:
        return '1E'
    elif x==5 and y==0:
        return '1F'
    elif x==6 and y==0:
        return '1G'
    elif x==7 and y==0:
        return '1H'
    elif x==0 and y==1:
        return '2A'
    elif x==1 and y==1:
        return '2B'
    elif x==2 and y==1:
        return '2C'
    elif x==3 and y==1:
        return '2D'
    elif x==4 and y==1:
        return '2E'
    elif x==5 and y==1:
        return '2F'
    elif x==6 and y==1:
        return '2G'
    elif x==7 and y==1:
        return '2H'
    elif x==0 and y==2:
        return '3A'
    elif x==1 and y==2:
        return '3B'
    elif x==2 and y==2:
        return '3C'
    elif x==3 and y==2:
        return '3D'
    elif x==4 and y==2:
        return '3E'
    elif x==5 and y==2:
        return '3F'
    elif x==6 and y==2:
        return '3G'
    elif x==7 and y==2:
        return '3H'
    elif x==0 and y==3:
        return '4A'
    elif x==1 and y==3:
        return '4B'
    elif x==2 and y==3:
        return '4C'
    elif x==3 and y==3:
        return '4D'
    elif x==4 and y==3:
        return '4E'
    elif x==5 and y==3:
        return '4F'
    elif x==6 and y==3:
        return '4G'
    elif x==7 and y==3:
        return '4H'
    elif x==0 and y==4:
        return '5A'
    elif x==1 and y==4:
        return '5B'
    elif x==2 and y==4:
        return '5C'
    elif x==3 and y==4:
        return '5D'
    elif x==4 and y==4:
        return '5E'
    elif x==5 and y==4:
        return '5F'
    elif x==6 and y==4:
        return '5G'
    elif x==7 and y==4:
        return '5H'
    elif x==0 and y==5:
        return '6A'
    elif x==1 and y==5:
        return '6B'
    elif x==2 and y==5:
        return '6C'
    elif x==3 and y==5:
        return '6D'
    elif x==4 and y==5:
        return '6E'
    elif x==5 and y==5:
        return '6F'
    elif x==6 and y==5:
        return '6G'
    elif x==7 and y==5:
        return '6H'
    elif x==0 and y==6:
        return '7A'
    elif x==1 and y==6:
        return '7B'
    elif x==2 and y==6:
        return '7C'
    elif x==3 and y==6:
        return '7D'
    elif x==4 and y==6:
        return '7E'
    elif x==5 and y==6:
        return '7F'
    elif x==6 and y==6:
        return '7G'
    elif x==7 and y==6:
        return '7H'
    elif x==0 and y==7:
        return '8A'
    elif x==1 and y==7:
        return '8B'
    elif x==2 and y==7:
        return '8C'
    elif x==3 and y==7:
        return '8D'
    elif x==4 and y==7:
        return '8E'
    elif x==5 and y==7:
        return '8F'
    elif x==6 and y==7:
        return '8G'
    elif x==7 and y==7:
        return '8H'

def Matching_rev(lastest):
    if lastest == '1A':
        return (0, 0)
    elif lastest == '1B':
        return (1, 0)
    elif lastest == '1C':
        return (2, 0)
    elif lastest == '1D':
        return (3, 0)
    elif lastest == '1E':
        return (4, 0)
    elif lastest == '1F':
        return (5, 0)
    elif lastest == '1G':
        return (6, 0)
    elif lastest == '1H':
        return (7, 0)
    elif lastest == '2A':
        return (0, 1)
    elif lastest == '2B':
        return (1, 1)
    elif lastest == '2C':
        return (2, 1)
    elif lastest == '2D':
        return (3, 1)
    elif lastest == '2E':
        return (4, 1)
    elif lastest == '2F':
        return (5, 1)
    elif lastest == '2G':
        return (6, 1)
    elif lastest == '2H':
        return (7, 1)
    elif lastest == '3A':
        return (0, 2)
    elif lastest == '3B':
        return (1, 2)
    elif lastest == '3C':
        return (2, 2)
    elif lastest == '3D':
        return (3, 2)
    elif lastest == '3E':
        return (4, 2)
    elif lastest == '3F':
        return (5, 2)
    elif lastest == '3G':
        return (6, 2)
    elif lastest == '3H':
        return (7, 2)
    elif lastest == '4A':
        return (0, 3)
    elif lastest == '4B':
        return (1, 3)
    elif lastest == '4C':
        return (2, 3)
    elif lastest == '4D':
        return (3, 3)
    elif lastest == '4E':
        return (4, 3)
    elif lastest == '4F':
        return (5, 3)
    elif lastest == '4G':
        return (6, 3)
    elif lastest == '4H':
        return (7, 3)
    elif lastest == '5A':
        return (0, 4)
    elif lastest == '5B':
        return (1, 4)
    elif lastest == '5C':
        return (2, 4)
    elif lastest == '5D':
        return (3, 4)
    elif lastest == '5E':
        return (4, 4)
    elif lastest == '5F':
        return (5, 4)
    elif lastest == '5G':
        return (6, 4)
    elif lastest == '5H':
        return (7, 4)
    elif lastest == '6A':
        return (0, 5)
    elif lastest == '6B':
        return (1, 5)
    elif lastest == '6C':
        return (2, 5)
    elif lastest == '6D':
        return (3, 5)
    elif lastest == '6E':
        return (4, 5)
    elif lastest == '6F':
        return (5, 5)
    elif lastest == '6G':
        return (6, 5)
    elif lastest == '6H':
        return (7, 5)
    elif lastest == '7A':
        return (0, 6)
    elif lastest == '7B':
        return (1, 6)
    elif lastest == '7C':
        return (2, 6)
    elif lastest == '7D':
        return (3, 6)
    elif lastest == '7E':
        return (4, 6)
    elif lastest == '7F':
        return (5, 6)
    elif lastest == '7G':
        return (6, 6)
    elif lastest == '7H':
        return (7, 6)
    elif lastest == '8A':
        return (0, 7)
    elif lastest == '8B':
        return (1, 7)
    elif lastest == '8C':
        return (2, 7)
    elif lastest == '8D':
        return (3, 7)
    elif lastest == '8E':
        return (4, 7)
    elif lastest == '8F':
        return (5, 7)
    elif lastest == '8G':
        return (6, 7)
    elif lastest == '8H':
        return (7, 7)