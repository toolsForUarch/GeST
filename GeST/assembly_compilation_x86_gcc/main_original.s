/*
Copyright 2019 ARM Ltd. and University of Cyprus
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

        .file   "main.s"
        .data
        .align 32
        .simdvalue:
            .long   0xaaaaaaaa
            .long   0x55555555
            .long   0x33333333
            .long   0xcccccccc
            .long   0xaaaaaaaa
            .long   0x55555555
            .long   0x33333333
            .long   0xcccccccc
        .text
        .globl  main
        main:
.LFB0:
        .cfi_startproc
        pushq   %rbp
        .cfi_def_cfa_offset 8
        .cfi_offset 5, -8
        movl    %esp, %ebp
        .cfi_def_cfa_register 5



        #reg init


        mov $0x55555555, %rax
        mov $0x33333333, %rbx
        mov $0x22222222, %rdx
        mov $0x44444444, %rsi
        mov $0x77777777, %rdi

        fldpi
        fldpi
        fldpi
        fldpi
        fldpi
        fldpi
        fldpi
        
        vmovdqa .simdvalue(%rip), %ymm0
        vmovdqa .simdvalue(%rip), %ymm1
        vmovdqa .simdvalue(%rip), %ymm2
        vmovdqa .simdvalue(%rip), %ymm3
        vmovdqa .simdvalue(%rip), %ymm4
        vmovdqa .simdvalue(%rip), %ymm5
        vmovdqa .simdvalue(%rip), %ymm6
        vmovdqa .simdvalue(%rip), %ymm7
        vmovdqa .simdvalue(%rip), %ymm8
        vmovdqa .simdvalue(%rip), %ymm9
        vmovdqa .simdvalue(%rip), %ymm10
        vmovdqa .simdvalue(%rip), %ymm11
        vmovdqa .simdvalue(%rip), %ymm12
        vmovdqa .simdvalue(%rip), %ymm13
        vmovdqa .simdvalue(%rip), %ymm14
        vmovdqa .simdvalue(%rip), %ymm15

        mov $50000000, %rcx  #leave for i--

        #subq    $304, %rsp

.L2:
      
#loop_code


        #sub $1,%rcx #remove this and below comment for fixed iterations
        #cmp $0, %rcx
        jmp     .L2

         leave
        .cfi_restore 5
        .cfi_def_cfa 4, 4
       ret

        .cfi_endproc
.LFE0:
        .ident  "GCC: (GNU) 6.4.0"
