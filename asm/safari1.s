SECTION "safari1", ROMX[$7D00]
;replicate original code
ld [$DBE4], a
;conserve registers
push af
push bc
push de
push hl

;our new code

;get destination
ld a, [$DBE4]
and a, 7
ld hl, $8D00
cp a, 0
jp z, destdone
ld de, $B0
dest:
add hl, de
dec a
jp nz, dest
destdone:
ld d, h
ld e, l

;get origin
ld a, [$DBE4]
ld hl, $0
cp a, 0
jp z, orgdone
ld bc, $B0
org:
add hl, bc
dec a
jp nz, org
orgdone:
ld bc, $4000
add hl, bc

push de
;load the graphics
ld a, $2D
ld bc, $B0
ld de, $A000
call $0F69

pop de
ld a, $00
ld bc, $B0
ld hl, $A000
call $0FBD

;restore registers and return
pop	hl
pop	de
pop	bc
pop	af
ret
