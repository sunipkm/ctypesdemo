ifeq ($(OS),Windows_NT)
# Windows NT is not supported
	$(error Windows NT not supported)
else 
#Determine Linux or Darwin
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		CC := gcc
		LIBEXT := so
		LINKOPT := -shared
	endif
	ifeq ($(UNAME_S),Darwin)
		CC := clang
		LIBEXT := dylib
		LINKOPT := -dynamiclib -single_module
	endif
endif
#Library Objects
lib_obj := src/adder.o
#All files
all: build build/adder.$(LIBEXT) TEST
#Build directory
build:
	mkdir build
#Objects
%.o: %.c 
	$(CC) -O2 -Wall -c $< -o $@
#Library
build/adder.$(LIBEXT): $(lib_obj)
	$(CC) $(lib_obj) -fPIC $(LINKOPT) -o $@
#Python test program
TEST: build/adder.$(LIBEXT)
	python exec/adder.py
clean:
	rm -rvf build