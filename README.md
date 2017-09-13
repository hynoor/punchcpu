# punchcpu
A tool in purpose of killing CPU to specific usage

### Work out number of CPU clocks per seconds?

f(h,i) = (h * 10^9 * 2) / i

where: 

`h:` CPU GHz

`2:` average number of instructions per clock of modern CPU

`I:` instructions per iteration




_>>>def iteration():_

    _for _ in xrange(100):_

        pass

_>>>dis.dis(iteration)_

_2   0  SETUP_LOOP          20 (to 23)_

    _3  LOAD_GLOBAL          0 (range)_

    _6  LOAD_CONST           1 (100)_

    _9  CALL_FUNCTION        1 (1 positional, 0 keyword pair)_ ##### 'yield roughly generates 50 machine instructions

    _12 GET_ITERA_

    _13 FOR_ITER             6 (to 22)_

    _16 STORE_FAST           0 (_)_

_3   19 JUMP_ABSOLUTE       13_

    _22 POP_BLOCK_

    _23 LOAD_CONST           0 (Nnoe)_

    _26 RETURN_VALUE_    
