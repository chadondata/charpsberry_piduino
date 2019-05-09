; My first assembly language code
; Like, for real, ever.
; Sum of Squares

; Data declarations
section         .data

; Constants
SUCCESS         equ 0   ; Successful OP
SYS_exit        equ 60  ; Terminate code

; Define data
n               dd  10
sumOfSquares    dq  0
msg             db  'Hello, world!', 0xa
len equ $ - msg

section         .text
global _start
_start:
; Compute sum of squares from 1 to n (inclusive)
; for (i=1; i<=n; i++) 
;   sumOfSquares += i^2
    mov edx, len
    mov ecx, msg
    mov ebx, 1
    mov eax, 4
    int 0x80
    
    mov rbx, 1
    mov ecx, dword [n]
sumLoop:
    mov rax, rbx
    mul rax
    add qword [sumOfSquares], rax
    inc rbx
    loop sumLoop

last:
    mov rax, SYS_exit
    mov rdi, SUCCESS
    syscall
