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
	.data

msg:
	.ascii	"\n"
len = . - msg
	.text
	.align 2
	.global main
	.type main, %function



main:

#reg init

    LDR x0,=0xAAAAAAAA 
    LDR x1,=0x55555555 
    LDR x2,=0x00000000  
    LDR x3,=0x00000000 
    LDR x4,=0x55555555  
    LDR x5,=0x33333333 
    LDR x6,=0xFFFFFFFF  
    LDR x7,=0xFFFFFFFE 
    LDR x8,=0x00000001  
    LDR x9,=0xCCCCCCCC
    LDR x10,=0xAAAAAAAA 
    LDR x11,=0x55555555 
    LDR x12,=0x00000000  
    LDR x13,=0x00000000 
    LDR x14,=0x55555555  
    LDR x15,=0x33333333 
    LDR x16,=0xFFFFFFFF  
    LDR x17,=0xFFFFFFFE 
    LDR x18,=0x00000001  
    LDR x19,=0xCCCCCCCC 
    LDR x20,=0xAAAAAAAA 
    LDR x21,=0x55555555 
    LDR x22,=0x00000000  
    LDR x23,=0x00000000 
    LDR x24,=0x55555555  
    LDR x25,=0x33333333 
    LDR x26,=0xFFFFFFFF  
    LDR x27,=0xFFFFFFFE 
    LDR x28,=0x00000001  
    LDR x29,=0xCCCCCCCC
    LDR x30,=0xCCCCCCCC  
    LDR D0,=0xAAAAAAAAAAAAAAAA 
    LDR D1,=0xFFFFFFFFFFFFFFFF   
    LDR D2,=0x5555555555555555   
    LDR D3,=0x3333333333333333   
    LDR D4,=0xCCCCCCCCCCCCCCCC   
    LDR D5,=0x0000000100000001   
    LDR D6,=0xFFFFFFFEFFFFFFFE   
    LDR D7,=0x0000000000000000   
    LDR D8,=0xAAAAAAAA55555555   
    LDR D9,=0x55555555AAAAAAAA
    LDR D10,=0xAAAAAAAAAAAAAAAA 
    LDR D11,=0xFFFFFFFFFFFFFFFF  
    LDR D12,=0x5555555555555555  
    LDR D13,=0x3333333333333333  
    LDR D14,=0xCCCCCCCCCCCCCCCC  
    LDR D15,=0x0000000100000001  
    LDR D16,=0xFFFFFFFEFFFFFFFE  
    LDR D17,=0x0000000000000000  
    LDR D18,=0xAAAAAAAA55555555  
    LDR D19,=0x55555555AAAAAAAA
    LDR D20,=0xAAAAAAAAAAAAAAAA 
    LDR D21,=0xFFFFFFFFFFFFFFFF  
    LDR D22,=0x5555555555555555  
    LDR D23,=0x3333333333333333  
    LDR D24,=0xCCCCCCCCCCCCCCCC  
    LDR D25,=0x0000000100000001  
    LDR D26,=0xFFFFFFFEFFFFFFFE  
    LDR D27,=0x0000000000000000  
    LDR D28,=0xAAAAAAAA55555555  
    LDR D29,=0x55555555AAAAAAAA
    LDR D30,=0x55555555AAAAAAAA
    


	LDR x12,=0x200
	#0x200 is 512 bytes
	SUB x12,sp,x12
	MOV x10,x12
	MOV x11,10
	#x12 will hold the end address
    
    LDR x28, =0x3B9ACA00/*1 billion iterations. x28 to be used for iteration counter if running for fixed iterations*/
    
Start:


    #loop_code




b Start
		
	#SUB x28,x28,1 #uncomment for running for fixed iterations
	#CBNZ x28,Start
		
ret
.size	main, .-main
.ident	"GCC: (APM-8.0.10-le) 4.9.3 20150218 (prerelease)"
.section	.note.GNU-stack,"",%progbits
