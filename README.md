# punchcpu

A tool in purpose of killing CPU to specific usage


**Work out number of CPU clocks per seconds?_**

_f(h,i) = (h * 10^9 * 2) / i_

where: 

`h:` CPU GHz

`2:` average number of instructions per clock of modern CPU

`I:` instructions per iteration


**Dissect Iteration**

```
def iteration():
    for _ in xrange(100):
        pass

dis.dis(iteration)
2   0  SETUP_LOOP          20 (to 23)
    3  LOAD_GLOBAL          0 (range)
    6  LOAD_CONST           1 (100)
    9  CALL_FUNCTION        1 (1 positional, 0 keyword pair)   # 'yield roughly generates 50 machine instructions
    12 GET_ITERA
    13 FOR_ITER             6 (to 22)
    16 STORE_FAST           0 (_)

3   19 JUMP_ABSOLUTE       13
    22 POP_BLOCK
    23 LOAD_CONST           0 (Nnoe)
    26 RETURN_VALUE
```
