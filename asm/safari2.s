SECTION "safari2", ROMX[$7D00]
;replicate original code
ld [$DBCC], a
;conserve registers
push af
push bc
push de
push hl

;our new code
ld a, [$DBC6]
cp a, 0
jp z, is0
dec a
is0:
ld [$DBE4], a

;get destination
ld a, [$DBE4]
and a, 7
ld hl, $8D00
cp a, 0
jp z, destdone1
ld de, $B0
dest1:
add hl, de
dec a
jp nz, dest1
destdone1:
ld d, h
ld e, l

;get origin
ld a, [$DBE4]
ld hl, $0
cp a, 0
jp z, orgdone1
ld bc, $B0
org1:
add hl, bc
dec a
jp nz, org1
orgdone1:
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


ld a, [$DBE4]
inc a
ld [$DBE4], a

;get destination
ld a, [$DBE4]
and a, 7
ld hl, $8D00
cp a, 0
jp z, destdone2
ld de, $B0
dest2:
add hl, de
dec a
jp nz, dest2
destdone2:
ld d, h
ld e, l

;get origin
ld a, [$DBE4]
ld hl, $0
cp a, 0
jp z, orgdone2
ld bc, $B0
org2:
add hl, bc
dec a
jp nz, org2
orgdone2:
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

ld a, [$DBE4]
inc a
ld [$DBE4], a

;get destination
ld a, [$DBE4]
and a, 7
ld hl, $8D00
cp a, 0
jp z, destdone3
ld de, $B0
dest3:
add hl, de
dec a
jp nz, dest3
destdone3:
ld d, h
ld e, l

;get origin
ld a, [$DBE4]
ld hl, $0
cp a, 0
jp z, orgdone3
ld bc, $B0
org3:
add hl, bc
dec a
jp nz, org3
orgdone3:
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

ld a, [$DBE4]
inc a
ld [$DBE4], a

;get destination
ld a, [$DBE4]
and a, 7
ld hl, $8D00
cp a, 0
jp z, destdone4
ld de, $B0
dest4:
add hl, de
dec a
jp nz, dest4
destdone4:
ld d, h
ld e, l

;get origin
ld a, [$DBE4]
ld hl, $0
cp a, 0
jp z, orgdone4
ld bc, $B0
org4:
add hl, bc
dec a
jp nz, org4
orgdone4:
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

ld a, [$DBE4]
inc a
ld [$DBE4], a

;get destination
ld a, [$DBE4]
and a, 7
ld hl, $8D00
cp a, 0
jp z, destdone5
ld de, $B0
dest5:
add hl, de
dec a
jp nz, dest5
destdone5:
ld d, h
ld e, l

;get origin
ld a, [$DBE4]
ld hl, $0
cp a, 0
jp z, orgdone5
ld bc, $B0
org5:
add hl, bc
dec a
jp nz, org5
orgdone5:
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





ld a, [$DBE4]
inc a
ld [$DBE4], a

;get destination
ld a, [$DBE4]
and a, 7
ld hl, $8D00
cp a, 0
jp z, destdone6
ld de, $B0
dest6:
add hl, de
dec a
jp nz, dest6
destdone6:
ld d, h
ld e, l

;get origin
ld a, [$DBE4]
ld hl, $0
cp a, 0
jp z, orgdone6
ld bc, $B0
org6:
add hl, bc
dec a
jp nz, org6
orgdone6:
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








ld a, [$DBE4]
inc a
ld [$DBE4], a

;get destination
ld a, [$DBE4]
and a, 7
ld hl, $8D00
cp a, 0
jp z, destdone7
ld de, $B0
dest7:
add hl, de
dec a
jp nz, dest7
destdone7:
ld d, h
ld e, l

;get origin
ld a, [$DBE4]
ld hl, $0
cp a, 0
jp z, orgdone7
ld bc, $B0
org7:
add hl, bc
dec a
jp nz, org7
orgdone7:
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
