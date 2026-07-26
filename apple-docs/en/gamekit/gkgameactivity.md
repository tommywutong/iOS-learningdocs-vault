---
title: GKGameActivity
framework: GameKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/gamekit/gkgameactivity
source_url: 'https://developer.apple.com/documentation/gamekit/gkgameactivity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/gamekit/gkgameactivity.json'
content_hash: 'sha256:15cf81e3e9277c89'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [GameKit](../gamekit.md)

# GKGameActivity

<sub>Class</sub>

An object that represents a single instance of a game activity for the current game.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class GKGameActivity
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an activity

- [- initWithDefinition:](<gkgameactivity/init(definition_).md>) — Creates a game activity with definition.
- [+ startWithDefinition:error:](<gkgameactivity/start(definition_).md>) — Creates and starts a game activity with a definition.
- [+ startWithDefinition:partyCode:error:](<gkgameactivity/start(definition_partycode_).md>) — Creates and starts a new game activity with a custom party code.

### Getting the activity definition

- [activityDefinition](gkgameactivity/activitydefinition.md) — The activity definition that this activity instance is based on.

### Getting the activity state

- [state](gkgameactivity/state-swift.property.md) — The state of the game activity.
- [State](gkgameactivity/state-swift.enum.md) — The state of a game activity.

### Updating the activity state

- [- start](<gkgameactivity/start().md>) — Starts the game activity if it’s not already started.
- [- pause](<gkgameactivity/pause().md>) — Pauses the game activity if it’s not already paused.
- [- resume](<gkgameactivity/resume().md>) — Resumes the game activity if it was paused.
- [- end](<gkgameactivity/end().md>) — Ends the game activity if it’s not already ended.

### Getting and removing achievements

- [achievements](gkgameactivity/achievements.md) — All achievements that have been associated with this activity.
- [- removeAchievements:](<gkgameactivity/removeachievements(__).md>) — Removes all achievements if they exist.
- [- getProgressOnAchievement:](<gkgameactivity/progress(on_).md>) — Get the achievement progress from a specific achievement of the local player if previously set.
- [- setProgressOnAchievement:toPercentComplete:](<gkgameactivity/setprogress(on_to_).md>) — Set a progress for an achievement for a player.
- [- setAchievementCompleted:](<gkgameactivity/setachievementcompleted(__).md>) — Set progress to 100% for an achievement for a player.

### Getting and removing leaderboard scores

- [leaderboardScores](gkgameactivity/leaderboardscores.md) — All leaderboard scores that have been associated with this activity.
- [- getScoreOnLeaderboard:](<gkgameactivity/score(on_).md>) — Get the leaderboard score from a specific leaderboard of the local player if previously set.
- [- setScoreOnLeaderboard:toScore:](<gkgameactivity/setscore(on_to_).md>) — Set a score of a leaderboard for a player.
- [- setScoreOnLeaderboard:toScore:context:](<gkgameactivity/setscore(on_to_context_).md>) — Set a score of a leaderboard with a context for a player.
- [- removeScoresFromLeaderboards:](<gkgameactivity/removescores(from_).md>) — Removes all scores from leaderboards for a player if exist.

### Getting and verifying the party code

- [partyCode](gkgameactivity/partycode.md) — If the game supports party code, this is the party code that can be shared among players to join the party.
- [partyURL](gkgameactivity/partyurl.md) — If the game supports party code, this is the URL that can be shared among players to join the party.
- [validPartyCodeAlphabet](gkgameactivity/validpartycodealphabet.md) — Allowed characters for the party code to be used to share this activity.
- [+ isValidPartyCode:](<gkgameactivity/isvalidpartycode(__).md>) — Checks whether a party code is in valid format.

### Getting the activity properties

- [duration](gkgameactivity/duration.md) — The total time elapsed while in active state.
- [startDate](gkgameactivity/startdate.md) — The date when the activity was initially started.
- [endDate](gkgameactivity/enddate.md) — The date when the activity was officially ended.
- [creationDate](gkgameactivity/creationdate.md) — The date when the activity was created.
- [lastResumeDate](gkgameactivity/lastresumedate.md) — The date when the activity was last resumed.

### Getting the custom user data

- [properties](gkgameactivity/properties.md) — Properties that contain additional information about the activity.

### Getting the activity identifiers

- [identifier](gkgameactivity/identifier.md) — The identifier of this activity instance.

### Checking for an activity

- [+ checkPendingGameActivityExistenceWithCompletionHandler:](<gkgameactivity/checkpendinggameactivityexistence(completionhandler_).md>) — Checks whether there is a pending activity to handle for the current game.

### Creating a matchmaking request

- [- makeMatchRequest](<gkgameactivity/makematchrequest().md>) — Makes a match request object with information from the activity, which you can use to find matches for the local player.

### Performing a matchmaking request

- [- findMatchWithCompletionHandler:](<gkgameactivity/findmatch(completionhandler_).md>) — Use information from the activity to find matches for the local player.
- [- findPlayersForHostedMatchWithCompletionHandler:](<gkgameactivity/findplayersforhostedmatch(completionhandler_).md>) — Use information from the activity to find server hosted players for the local player.

## See Also

### Activities

- [Creating activities for your game](creating-activities-for-your-game.md) — Use activities to surface game content to players and encourage them to connect with each other.
- [GKGameActivityDefinition](gkgameactivitydefinition.md) — An object that represents the static metadata you define for the activity.
- [GKGameActivityListener](gkgameactivitylistener.md) — An object that responds to activity events.
