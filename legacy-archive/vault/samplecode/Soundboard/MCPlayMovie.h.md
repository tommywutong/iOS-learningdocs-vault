---
title: Soundboard
apple_id: DTS10000059
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Soundboard/Listings/MCPlayMovie_h.html
archived_at: '2026-07-18T03:25:14.098883Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Soundboard](Soundboard.md)


[Next](Document%20Revision%20History.md)[Previous](GWLayers.h.md)

# MCPlayMovie.h

```c
/*
  File:         MCPlayMovie.h
  Contains:     Header for movie Playing Application Using Movie Controllers.
  Written by:   John Wang / DTS, Tim Nufire
  Copyright:    © 1991-1995 by Apple Computer, Inc., all rights reserved.
*/

#ifndef _MCPLAYMOVIE_
#define _MCPLAYMOVIE_

#include    <Palettes.h>

// DEFINES
#define Gestalttest     0xA1AD
#define NoTrap          0xA89F

#define MAXMOVIES       5


// FUNCTION PROTOTYPES
Movie GetMovieFromFile(void);
OSErr PlayMovie(int index);
Boolean InitMovies(void);
void FinishMovies(void);
Boolean DoCloseMovieCommand(void);
int PlayMovies(EventRecord* myEvent);
void DoOpenMovieCommand(void);

// GLOBALS
extern Boolean playingMovie[MAXMOVIES];
extern Movie myMovie[MAXMOVIES];
extern WindowPtr movieWindow[MAXMOVIES];
extern MovieController mcPlay[MAXMOVIES];
extern int startlocation;
extern CTabHandle mycolors;
extern PaletteHandle srcPalette;

#endif _MCPLAYMOVIE_
```

[Next](Document%20Revision%20History.md)[Previous](GWLayers.h.md)

