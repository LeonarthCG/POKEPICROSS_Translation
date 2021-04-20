SECTION "pokedex1", ROMX[$7D00]
;replicate original code
add	hl, de
ld de, $D6D5
;conserve registers
push af
push bc
push de
push hl

;our new code

;check if we are not in the list
ld a, [$DBCC]
cp a, 0
jp z, end

;get destination
ld a, [$DBE4]
and a, 7
ld hl, $9000
cp a, 0
jp z, destdone
ld de, $50
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
ld bc, $50
org:
add hl, bc
dec a
jp nz, org
orgdone:
ld bc, $4000
add hl, bc

push de
;load the graphics
ld a, $2C
ld bc, $50
ld de, $A000
call $0F69

pop de
ld a, $00
ld bc, $50
ld hl, $A000
call $0FBD

;restore registers and return
end:
pop	hl
pop	de
pop	bc
pop	af
ret
