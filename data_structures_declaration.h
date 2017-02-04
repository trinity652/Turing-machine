#ifndef __turing_h__
#define __turing_h__

#define MAX_TRANSITIONS 5 //Represents the number of states the state diagram has
#define MAX_STATES 25

// forward declare structs
struct State;
struct Transition;

typedef enum
/*These are state variables the header on the tape moves depending
upon the state */
{
    LEFT, RIGHT
} Direction;

typedef enum
/* The given structure has been defined to detect if the given symbol
gets accepted or rejected*/
{
    FALSE, TRUE
} Bool;

struct Transition
/*The structure to store the set defined by the transition function of the
Turing  Machine,M */
{
    char input;
    char write;
    Direction move;
    struct State *next;
};

typedef struct Transition Transition;

struct State
/*The structure to store the set containing information about the current state
of the Turing Machine,M */
{
    int id;
    int trans_count;
    struct Transition* transitions[ MAX_TRANSITIONS ];
    Bool accept;
    Bool reject;
};

typedef struct State State;

struct Turing
/*The structure to store the information about how many transitions
occur in the given Turing Machine after an input is given before it is rejected
or accepted.
*/
{
    int state_count;
    State* states[ MAX_STATES ];
    State* current;
    int head;
};

typedef struct Turing Turing;

#endif
