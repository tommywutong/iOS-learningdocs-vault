---
title: GlyphaIVOld
apple_id: DTS10000053
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/GlyphaIVOld/Listings/G4Interface_c.html
archived_at: '2026-07-18T03:10:51.494527Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GlyphaIVOld](GlyphaIVOld.md)


[Next](G4Lava.c.md)[Previous](G4Graphics.c.md)

# G4Interface.c

```c
/*
    File:       G4Interface.c

    Contains:   xxx put contents here xxx

    Version:    xxx put version here xxx

    Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                xxx put dri here xxx

        Other Contact:      xxx put other contact here xxx

        Technology:         xxx put technology here xxx

    Writers:

        (sjb)   Steve Bollinger

    Change History (most recent first):

         <2>      7/1/98    sjb     Update to CWPro 2
*/


//============================================================================
//----------------------------------------------------------------------------
//                                  Interface.c
//----------------------------------------------------------------------------
//============================================================================

// I put all interface related code in here.  Interface would include eventÉ
// handling, menus, dialog boxes, etc.  All the user interaction that takesÉ
// place before and after an actual game is in play.

#include "G4Externs.h"
#include <Sound.h>
#include <Devices.h>
#include <AppleEvents.h>
#include <ToolUtils.h>

#define kAppleMenuID        128
#define iAbout              1
#define kGameMenuID         129
#define iNewGame            1
#define iPauseGame          2
#define iEndGame            3
#define iQuit               5
#define kOptionsMenuID      130
#define iSettings           1
#define iHelp               2
#define iHighScores         3
#define kAboutPictID        132


void DoAppleMenu (short);
void DoGameMenu (short);
void DoOptionsMenu (short);
void UpdateMainWindow (void);
void HandleMouseEvent (EventRecord *);
void HandleKeyEvent (EventRecord *);
void HandleUpdateEvent (EventRecord *);
void HandleOSEvent (EventRecord *);
void HandleHighLevelEvent (EventRecord *);
void DoAbout (void);
void DoGameSettings (void);
void DrawBanner(void);

Rect        mainWindowRect;


MenuHandle  appleMenu, gameMenu, optionsMenu;
Boolean     switchedOut, quitting, canPlay, openTheScores;

extern  prefsInfo   thePrefs;
extern  Rect        backSrcRect, workSrcRect;
extern  CGrafPtr    backSrcMap, workSrcMap;
extern  Boolean     pausing, playing, helpOpen, scoresOpen;


//==============================================================  Functions
//--------------------------------------------------------------  MenusReflectMode

// Depending on whether a game is in progress (paused) or not, I wantÉ
// menu items grayed out in one case and not grayed out in the other.
// This function, when called, displays the menus correctly dependingÉ
// on the mode we're in (playing or not playing, pausing or not).

void MenusReflectMode (void)
{
    if (playing)                                // If a game is in progressÉ
    {
        DisableItem(gameMenu, iNewGame);        // Cannot begin another New Game.
        EnableItem(gameMenu, iPauseGame);       // Can Pause Game.
        if (pausing)                            // If we are pausedÉ
            SetMenuItemText(gameMenu, iPauseGame, 
                    "\pResume Game");           // Rename item "Resume Game".
        else                                    // If we are not pausedÉ
            SetMenuItemText(gameMenu, iPauseGame, 
                    "\pPause Game");            // Rename item "Pause Game".
        EnableItem(gameMenu, iEndGame);         // Can End Game.
        DisableItem(optionsMenu, 0);            // Cannot change game settings.
    }
    else                                        // Else, if Glypha is idleÉ
    {
        EnableItem(gameMenu, iNewGame);         // Can begin a New Game.
        DisableItem(gameMenu, iPauseGame);      // Cannot Pause Game.
        SetMenuItemText(gameMenu, iPauseGame, 
                "\pPause Game");                // Rename item "Pause Game".
        DisableItem(gameMenu, iEndGame);        // Cannot End Game.
        EnableItem(optionsMenu, 0);             // Can change game settings.
    }
}

//--------------------------------------------------------------  DoAppleMenu

// This function takes care of handling the Apple menu (Desk Assecories and theÉ
// About box).

void DoAppleMenu (short theItem)
{
    Str255      daName;
    GrafPtr     wasPort;
    short       daNumber;

    switch (theItem)                            // Depending on the item selectedÉ
    {
        case iAbout:                            // If the About item was selectedÉ
        if ((scoresOpen) || (helpOpen))         // If high scores or help screens upÉ
        {
            CloseWall();                        // hide them.
            scoresOpen = FALSE;                 // High scores no longer open.
            helpOpen = FALSE;                   // Help screen is no longer open.
                                                // Uncheck help & high scores menu items.
            CheckItem(optionsMenu, iHelp, helpOpen);
            CheckItem(optionsMenu, iHighScores, scoresOpen);
        }
        DoAbout();                              // Bring up the About dialog.
        break;

        default:                                // If any other item was selected (DA)É
        GetMenuItemText(appleMenu, theItem, daName);    // Get the name of the item selected.
        GetPort(&wasPort);                      // Remember our port.
        daNumber = OpenDeskAcc(daName);         // Launch the Desk Accesory.
        SetPort((GrafPtr)wasPort);              // When we return, restore port.
        break;
    }
}

//--------------------------------------------------------------  DoGameMenu

// This function handles a users interaction with the Game menu.  QuittingÉ
// Glypha, starting a new game, resuming a paused game are handled here.

void DoGameMenu (short theItem)
{
    switch (theItem)                        // Depending on menu item selectedÉ
    {
        case iNewGame:                      // If user selected New Game itemÉ
        if ((scoresOpen) || (helpOpen))     // If high scores or help screen is up,É
        {                                   // close them first.
            CloseWall();
            scoresOpen = FALSE;
            helpOpen = FALSE;
            CheckItem(optionsMenu, iHelp, helpOpen);
            CheckItem(optionsMenu, iHighScores, scoresOpen);
        }
        InitNewGame();                      // Initialize variables for a new game.
        MenusReflectMode();                 // Properly gray out the right menu items.
        break;

        case iPauseGame:                    // If user selected Pause Game itemÉ
        if (pausing)                        // If we are paused, resume playing.
        {
            pausing = FALSE;                // Turn off pausing flag.
            DumpBackToWorkMap();            // Restore off screen just in case.
        }                                   // Actually pausing a game (not resuming)É
        break;                              // is not really handled here.  It's handledÉ
                                            // directly within the main game loop.

        case iEndGame:                      // Ending a game in progress isn't reallyÉ
        break;                              // handled here - this is a dummy item.
                                            // Ending a game is handled within the mainÉ
                                            // game loop by looking for the 'command'É
                                            // and 'E' key explicitly.

        case iQuit:                         // If user selected Quit itemÉ
        quitting = TRUE;                    // Set quitting flag to TRUE.
        break;
    }
}

//--------------------------------------------------------------  DoOptionsMenu

// This function handles the Options menu.  Options include game settings,É
// displaying the high scores, and bringing up the Help screen.

void DoOptionsMenu (short theItem)
{
    switch (theItem)                    // Depending on which item the user selectedÉ
    {
        case iSettings:                 // If user selected Game Settings itemÉ
        if ((scoresOpen) || (helpOpen)) // Close high scores or help screen.
        {
            CloseWall();
            scoresOpen = FALSE;
            helpOpen = FALSE;
            CheckItem(optionsMenu, iHelp, helpOpen);
            CheckItem(optionsMenu, iHighScores, scoresOpen);
        }
        DoGameSettings();               // Bring up game settings dialog.
        break;

        case iHelp:                     // If user selected Help itemÉ
        if (helpOpen)                   // If Help open, close it.
        {
            CloseWall();
            helpOpen = FALSE;
        }
        else                            // Else, if Help is not open - open it.
        {
            if (scoresOpen)             // If the High Scores are up though,É
            {
                CloseWall();            // Close them first.
                scoresOpen = FALSE;
                CheckItem(optionsMenu, iHighScores, scoresOpen);
            }
            OpenHelp();                 // Now open the Help screen.
        }
        CheckItem(optionsMenu, iHelp, helpOpen);
        break;

        case iHighScores:               // If user selected High ScoresÉ
        if (scoresOpen)                 // If the High Scores are up, close them.
        {
            CloseWall();
            scoresOpen = FALSE;
        }
        else                            // If the High Scores are not upÉ
        {
            if (helpOpen)               // First see if Help is open.
            {
                CloseWall();            // And close the Help screen.
                helpOpen = FALSE;
                CheckItem(optionsMenu, iHelp, helpOpen);
            }
            OpenHighScores();           // Now open the High Scores.
        }
        CheckItem(optionsMenu, iHighScores, scoresOpen);
        break;
    }
}

//--------------------------------------------------------------  DoMenuChoice

// This is the main menu-handling function.  It examines which menu was selectedÉ
// by the user and passes on to the appropriate function, the item within thatÉ
// menu that was selected.

void DoMenuChoice (long menuChoice)
{
    short       theMenu, theItem;

    if (menuChoice == 0)            // A little error checking.
        return;

    theMenu = HiWord(menuChoice);   // Extract which menu was selected.
    theItem = LoWord(menuChoice);   // Extract which item it was that was selected.

    switch (theMenu)                // Now, depending upon which menu was selectedÉ
    {
        case kAppleMenuID:          // If the Apple menu selectedÉ
        DoAppleMenu(theItem);       // Call the function that handles the Apple menu.
        break;

        case kGameMenuID:           // If the Game menu selectedÉ
        DoGameMenu(theItem);        // Call the function that handles the Game menu.
        break;

        case kOptionsMenuID:        // If the Options menu selectedÉ
        DoOptionsMenu(theItem);     // Call the function that handles the Options menu.
        break;
    }

    HiliteMenu(0);                  // "De-invert" menu.
}

//--------------------------------------------------------------  UpdateMainWindow

// This is a simple function that simply copies the contents from theÉ
// background offscreen pixmap to the main screen.  It is primarilyÉ
// called in response to an update event, but could be called any timeÉ
// when I want to force the screen to be redrawn.

void UpdateMainWindow (void)
{
    OSStatus theError;

    theError = DSpContext_GetBackBuffer( gTheContext, kDSpBufferKind_Normal, &workSrcMap );
    if( theError )
    {
        DSpContext_Release( gTheContext );
        gTheContext = NULL;
        RedAlert("\pUnable to get back buffer");
    }

    CopyBits(&((GrafPtr)backSrcMap)->portBits, 
            &(((GrafPtr)workSrcMap)->portBits), 
            &mainWindowRect, &mainWindowRect, 
            srcCopy, 0L);

    DSpContext_SwapBuffers( gTheContext, NULL, NULL );
}

//--------------------------------------------------------------  HandleMouseEvent

// Mouse clicks come here.  This is standard event-handling drivel.  No different 
// from any other standard Mac program (game or otherwise).

void HandleMouseEvent (EventRecord *theEvent)
{
    WindowPtr   whichWindow;
    long        menuChoice;
    short       thePart;
                                                // Determine window and where in window.
    thePart = FindWindow(theEvent->where, &whichWindow);

    switch (thePart)                            // Depending on where mouse was clickedÉ
    {
        case inSysWindow:                       // In a Desk Accesory.
        SystemClick(theEvent, whichWindow);     // (Is this stuff obsolete yet?)
        break;

        case inMenuBar:                         // Selected a menu item.
        menuChoice = MenuSelect(theEvent->where);
        if (canPlay)                            // Call menu handling routine.
            DoMenuChoice(menuChoice);
        break;

        case inDrag:                            // Like the lazy bastard I amÉ
        case inGoAway:                          // I'll just ignore these.
        case inGrow:                            // But, hey, the window isn'tÉ
        case inZoomIn:                          // movable or growable!
        case inZoomOut:
        break;

        case inContent:                         // Click in the window itself.
        if (!playing)
        {
            short h = theEvent->where.h;
            short v = theEvent->where.v;
            short count = 10;

            while(count > 0)
            {
                StartPixelShatter(h, v, 0, 0, kShatterLightningDust);
                count--;
            }

            lightH = h;
            lightV = v;
            lightningCount = 15;
            PlayExternalSound(kLightningSound, kLightningPriority);
        }
        break;
    }
}

//--------------------------------------------------------------  HandleKeyEvent

// More standard issue.  This function handles any keystrokes when no game is
// in session.  Command-key strokes handled here too.

void HandleKeyEvent (EventRecord *theEvent)
{
    char        theChar;
    Boolean     commandDown;

    theChar = theEvent->message & charCodeMask;             // Extract key hit.
    commandDown = ((theEvent->modifiers & cmdKey) != 0);    // See if command key down.

    if (commandDown)                                // If command key down, call menuÉ
    {                                               // handling routine.
        if (canPlay)
            DoMenuChoice(MenuKey(theChar));
    }
    else
    {
        if (helpOpen)                               // Handle special keys if the helpÉ
        {                                           // screen is up.
            if (theChar == kUpArrowKeyASCII)        // Up arrow key scrolls help down.
            {
                if (theEvent->what == autoKey)
                    ScrollHelp(-3);
                else
                    ScrollHelp(-1);
            }
            else if (theChar == kDownArrowKeyASCII) // Down arrow key scrolls help up.
            {
                if (theEvent->what == autoKey)
                    ScrollHelp(3);
                else
                    ScrollHelp(1);
            }
            else if (theChar == kPageDownKeyASCII)  // Handle page down for help screen.
            {
                ScrollHelp(199);
            }
            else if (theChar == kPageUpKeyASCII)    // Handle page up for help.
            {
                ScrollHelp(-199);
            }
            else if ((theChar == kHelpKeyASCII) && (!playing))
            {                                       // Hitting Help key closes helpÉ
                CloseWall();                        // (if it's already open).
                helpOpen = FALSE;
                CheckItem(optionsMenu, iHelp, helpOpen);
            }
        }
        else if ((theChar == kHelpKeyASCII) && (!playing))
        {                                           // Else, if help not open and HelpÉ
            if (scoresOpen)                         // key is hit, open Help.
            {                                       // Close high scores if open.
                CloseWall();
                scoresOpen = FALSE;
                CheckItem(optionsMenu, iHighScores, scoresOpen);
            }
            OpenHelp();                             // Open help.
            CheckItem(optionsMenu, iHelp, helpOpen);
        }
    }
}

//--------------------------------------------------------------  HandleUpdateEvent

// This function handles update events.  Standard event-handling stuff.

void HandleUpdateEvent (EventRecord *theEvent)
{   
#if !GENERATINGPOWERPC
    if ((WindowPtr)theEvent->message == mainWindow)
    {
        SetPort((GrafPtr)mainWindow);       // Don't forget this line, BTW.
        BeginUpdate((GrafPtr)mainWindow);   // I did once and it took meÉ
        UpdateMainWindow();                 // ages to track down that bug.
        EndUpdate((GrafPtr)mainWindow);     // Well, it took me a week I think.
        canPlay = TRUE;
    }
#endif
}

//--------------------------------------------------------------  HandleOSEvent

// Handle switchin in and out events.  Standard event-handling stuff.

void HandleOSEvent (EventRecord *theEvent)
{   
    if (theEvent->message & 0x01000000)     // If suspend or resume eventÉ
    {
        if (theEvent->message & 0x00000001) // Specifically, if resume eventÉ
            switchedOut = FALSE;            // I keep thinking I should do more here.
        else                                // Or if suspend eventÉ
            switchedOut = TRUE;             // What am I forgetting?
    }
}

//--------------------------------------------------------------  HandleHighLevelEvent

// Again, it's a fact I'm lazy.  AppleEvents are fairly easy to implement butÉ
// a nightmare to try and explain.  Filling out the below function is left asÉ
// and exercise to the reader.

void HandleHighLevelEvent (EventRecord *theEvent)
{   
//  theErr = AEProcessAppleEvent(theEvent);
}

//--------------------------------------------------------------  HandleEvent

// Standard event stuff.  This is the culling function that calls all the aboveÉ
// functions.  It looks for an event and if it detects one, it calls the appropriateÉ
// function above to handle it.

void HandleEvent (void)
{
    EventRecord theEvent;
    long        sleep = 0L;
    Boolean     itHappened;
                                            // See if an event is queued up.
#if GENERATINGPOWERPC
        canPlay = TRUE;
#endif

    itHappened = WaitNextEvent(everyEvent, &theEvent, sleep, 0L);

    if (itHappened)                         // Ah, an event.  I live for events!
    {
        switch (theEvent.what)              // And what kind of event be ya'?
        {
            case mouseDown:                 // Aiy!  Y' be a mouse click do ya'?
            HandleMouseEvent(&theEvent);
            break;

            case keyDown:                   // Key down, key held down events.
            case autoKey:
            HandleKeyEvent(&theEvent);
            break;

            case updateEvt:                 // Something needs redrawing!
            HandleUpdateEvent(&theEvent);
            break;

            case osEvt:                     // Switching in and out events.
            HandleOSEvent(&theEvent);
            break;

            case kHighLevelEvent:           // Hmmmm.  A "what" event?
            HandleHighLevelEvent(&theEvent);
            break;

            default:
            break;
        }
    }


#if 0
    else if (openTheScores)                 // Check for "auto open" flag.
    {                                       // If TRUE, set the flag back toÉ
        openTheScores = FALSE;              // FALSE and open the high scores.
        OpenHighScores();
    }
#endif
}

//--------------------------------------------------------------  DoAbout

// This handles the About dialog.  It brings up the About box in aÉ
// simple centered window with no drag bar, close box or anything.
// Leaving the dialog is handled with a simple mouse click.

void DoAbout (void)
{
    Rect        aboutRect;
    WindowPtr   aboutWindow;

    SetRect(&aboutRect, 0, 0, 325, 318);        // Bring up centered window.
    CenterRectInRect(&aboutRect, &qd.screenBits.bounds);
    aboutWindow = GetNewCWindow(129, 0L, kPutInFront);
    MoveWindow((GrafPtr)aboutWindow, aboutRect.left, aboutRect.top, TRUE);
    ShowWindow((GrafPtr)aboutWindow);
    SetPort((GrafPtr)aboutWindow);
    LoadGraphic(kAboutPictID);                  // Draw About dialog graphic.

    do                                          // Make sure button not downÉ
    {                                           // before proceeding.
    }
    while (Button());                           // Proceed.
    do                                          // And now wait until the mouseÉ
    {                                           // is pressed before closing theÉ
    }                                           // window (ABout dialog).
    while (!Button());

    FlushEvents(everyEvent, 0);                 // Flush the queue.

    if (aboutWindow != 0L)
        DisposeWindow(aboutWindow);             // Close the About dialog.
}

//--------------------------------------------------------------  DoGameSettings

// This one however is a good and proper dialog box.  It handles the meagerÉ
// preference settings for Glypha.  Nothing fancy here to report.  Just aÉ
// straight-forward dialog calling routine.

void DoGameSettings (void)
{
    #define     kGameSettingsDialogID   133
    DialogPtr   theDial;
    long        newVolume;
    short       i, item;
    Boolean     leaving;

    CenterDialog(kGameSettingsDialogID);    // Center dialog, then call up.
    theDial = GetNewDialog(kGameSettingsDialogID, 0L, kPutInFront);
    SetPort((GrafPtr)theDial);
    ShowWindow((GrafPtr)theDial);           // Make visible (after centering).
    DrawDefaultButton(theDial);             // Draw border around Okay button.
    FlushEvents(everyEvent, 0);
                                            // Put in a default sound volume.
    SetDialogNumToStr(theDial, 3, (long)thePrefs.wasVolume);
    SelectDialogItemText(theDial, 3, 0, 1024);  // Select it.

    leaving = FALSE;

    while (!leaving)
    {
        ModalDialog(0L, &item);             // Simple modal dialog filtering.

        if (item == 1)                      // Did user hit the Okay button?
        {                                   // Well see if volume entered is legal.
            GetDialogNumFromStr(theDial, 3, &newVolume);
            if ((newVolume >= 0) && (newVolume <= 7))
            {                               // If it is legal, we'll note it and quit.
                thePrefs.wasVolume = newVolume * (0x01000000 / 7) + newVolume * (0x0100 / 7);
                SetDefaultOutputVolume (thePrefs.wasVolume);            // get new volume
//              SetSoundVol((short)newVolume);
                leaving = TRUE;             // Bye.
            }
            else                            // Otherwise, the volume entered is wrong.
            {                               // So we'll Beep, enter the last legalÉ
                SysBeep(1);                 // value and select the text again.
                SetDialogNumToStr(theDial, 3, (long)thePrefs.wasVolume);
                SelectDialogItemText(theDial, 3, 0, 1024);
            }
        }
        else if (item == 2)                 // Did the user hit the "Clear Scores"É
        {                                   // button?
            for (i = 0; i < 10; i++)        // Walk through and zero scores.
            {
                PasStringCopy("\pNemo", thePrefs.highNames[i]);
                thePrefs.highScores[i] = 0L;
                thePrefs.highLevel[i] = 0;
                openTheScores = TRUE;       // Bring up scores when dialog quits.
            }
            DisableControl(theDial, 2);     // Gray out Clear Scores button.
        }
    }

    DisposeDialog(theDial);                 // Clean up before going.
}
```

[Next](G4Lava.c.md)[Previous](G4Graphics.c.md)

