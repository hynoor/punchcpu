# punchcpu

A handy tool on purpose of killing CPU to specific usage, support both Linux and Windows systems


**_Usage_**

For instance, killng CPU usage to 75% percents:
```
$ python punchcpu.py 75 
CPU MHz: 2294
CPU cores: 2
CPU usage: 80

started process on core 0 ...
started process on core 1 ...

CPU clocks per second: 2294000000
started process on core 0 ...

CPU clocks per second: 2294000000
started process on core 1 ...
```

**_Work out number of CPU clocks per seconds?_**

```
f(h, i) = (h * 10^9 * 2) / i

where: 
h: CPU GHz
2: average number of instructions per clock of modern CPU
I: instructions per iteration
```

**_Dissect Iteration_**

```
def iteration():
    for _ in xrange(100):
        pass

dis.dis(iteration)
2   0  SETUP_LOOP          20 (to 23)
    3  LOAD_GLOBAL          0 (range)
    6  LOAD_CONST           1 (100)
    9  CALL_FUNCTION        1 (1 positional, 0 keyword pair)   # 'yield' roughly generates 50 machine instructions
    12 GET_ITER
    13 FOR_ITER             6 (to 22)
    16 STORE_FAST           0 (_)

3   19 JUMP_ABSOLUTE       13
    22 POP_BLOCK
    23 LOAD_CONST           0 (Nnoe)
    26 RETURN_VALUE
```
