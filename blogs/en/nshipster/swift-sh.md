---
title: swift-sh
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/swift-sh/'
original_language: en
published: 2019-01-14
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:bc28c3bb8db2c7ee'
translated: false
---

> 原文：[swift-sh](https://nshipster.com/swift-sh/)　·　NSHipster (Mattt)

# [swift-sh](https://nshipster.com/swift-sh/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  January 14^th, 2019

Swift is a fast, safe, modern programming language with an open governance model and a vibrant community. There’s no reason that it should be limited to _just_ making apps. And indeed, many smart people are working hard to [bring Swift to new platforms](https://forums.swift.org/t/windows-nightlies/19174/1) and evolve its capabilities for [web development](https://swift.org/server/) and [machine learning](https://www.tensorflow.org/swift/).

Scripting is another point of interest for the Swift community, but the amount of setup required to use 3rd-party libraries has long been seen as a non-starter.

…that is, until now.

On Friday, [Max Howell](https://twitter.com/mxcl/) [announced](https://twitter.com/mxcl/status/1083942251003297794) a new project called [swift-sh](https://github.com/mxcl/swift-sh). It provides a shim around the Swift compiler that creates a package for your script and uses it to automatically add and manage external dependencies imported with a special trailing comment.

Although in its initial stages of development, it’s already seemingly managed to solve the biggest obstacle to Swift becoming a productive scripting language.

This week, let’s take a very early look at this promising new library and learn how to start using it today to write Swift scripts.

## Installation and Setup

Assuming you have Swift and Xcode on your system, you can install `swift-sh` with [Homebrew](https://nshipster.com/homebrew/) using the following command:

```
$ brew install mxcl/made/swift-sh
```

## Example Usage

The original [Swift Package Manager](https://swift.org/package-manager/) examples provided a [shuffleable](https://github.com/apple/example-package-fisheryates) [`Deck`](https://github.com/apple/example-package-deckofplayingcards) of [`PlayingCard`](https://github.com/apple/example-package-playingcard) values. So it feels appropriate to revisit them here. For this example, let’s build a Swift script to deal and print out a formatted representation of a hand of [Bridge](https://en.wikipedia.org/wiki/Contract_bridge). The final result should look something like this:

♠ 10 9 8 7

♥ 6 5 4 3

♦ —

♣ 7 6 5 3 2

♠ 6 5 4 3 2

**M**  
   
 **Meyer Drax**  
   
 **Bond**

♠ A K Q J

♥ 10 9 8 7 2

♥ A K Q J

♦ J 10 2

♦ A K

♣ —

♣ K J 9

♠ —

♥ —

♦ Q 8 7 6 5 4 3 2

♣ A Q 10 8 4

### Importing Dependencies

Start by creating a new `.swift` file with a shebang at the beginning _(more on that later)_.

```
$ echo '#!/usr/bin/swift sh' > bridge.swift
```

Next, add import declarations for three modules: `DeckOfPlayingCards`, `PlayingCard`, and `Cycle`.

```
import DeckOfPlayingCards // @NSHipster ~> 4.0.0
import PlayingCard
import Cycle // @NSHipster == bb11e28
```

The comment after the import declaration for `DeckOfPlayingCards` tells `swift-sh` to look for the package on GitHub in a repository by the same name under the [`NSHipster`](https://github.com/NSHipster) username. The tilde-greater-than operator in `~> 4.0.0` is shorthand for specifying a version “equal to or greater than in the least significant digit” according to [Semantic Versioning](https://semver.org) conventions. In this case, Swift Package Manager will use the latest release whose major is equal to `4` and minor release is equal to `0` (that is, it will use `4.0.1` or`4.0.0`, but not `4.1.0` or `5.0.0`).

For the `PlayingCard` module, we don’t have to add an import specification for because it’s already included as a dependency of `DeckOfPlayingCards`.

Finally, the `Cycle` module is an external package and includes an external import specification that tells `swift-sh` how to add it as a dependency. The notable difference here is that the `==` operator is used to specify a revision rather than a tagged release.

### Recruiting Players

With all of our dependencies accounted for, we have everything we need to write our script.

First, create a `Player` class, consisting of `name` and `hand` properties.

```
class Player {
    var name: String
    var hand: [PlayingCard] = []

    init(name: String) {
        self.name = name
    }
}
```

In an extension, conform `Player` to `CustomStringConvertible` and implement the `description` property, taking advantage of the convenient [`Dictionary(grouping:by:)`](https://developer.apple.com/documentation/swift/dictionary/2995342-init) initializer [added to Swift 4](https://swift.org/blog/dictionary-and-set-improvements/). By convention, a player’s hand is grouped by suit and ordered by rank.

```
extension Player: CustomStringConvertible {
    var description: String {
        var description = "\(name):"

        let cardsBySuit = Dictionary(grouping: hand) { $0.suit }
        for (suit, cards) in cardsBySuit.sorted(by: { $0.0 > $1.0 }) {
            description += "\t\(suit) "
            description += cards.sorted(by: >)
                                .map{ "\($0.rank)" }
                                .joined(separator: " ")
            description += "\n"
        }

        return description
    }
}
```

### Shuffling and Dealing the Deck

Create and shuffle a standard deck of 52 playing cards, and initialize players at each of the four cardinal directions.

```
var deck = Deck.standard52CardDeck()
deck.shuffle()

var north = Player(name: "North")
var west = Player(name: "West")
var east = Player(name: "East")
var south = Player(name: "South")
```

In Bridge, cards are dealt one-by-one to each player until no cards remain. We use the `cycled()` method to rotate between each of our players to ensure an even and fair deal.

```
let players = [north, east, west, south]
var round = players.cycled()

while let card = deck.deal(),
    let player = round.next()
{
    player.hand.append(card)
}
```

After the cards are dealt, each player has 13 cards.

```
for player in players {
    print(player)
}
```

### Running the Card Game

We can run our completed Swift script from the command line by passing the file as an argument to the `swift sh` subcommand.

Behind the scenes, `swift-sh` creates a Swift package and tells the Swift Package Manager to fetch the dependencies for each commented import declaration (here, `DeckOfPlayingCards` and `Cycle`), and build an executable using those modules.

Running our project, the formatted description we implemented above for each of the players, as expected.

```
$ swift sh ./bridge.swift
North:  ♠︎ K 10 9 8 5 4
        ♡ K 3
        ♢ A 10
        ♣︎ A 4 2

West:   ♠︎ J 3 2
        ♡ 9 6 5
        ♢ Q 9 8 3 2
        ♣︎ 6 5

East:   ♠︎ Q 7
        ♡ A J 10 7 4
        ♢ K 5 4
        ♣︎ 10 7 3

South:  ♠︎ A 6
        ♡ Q 8 2
        ♢ J 7 6
        ♣︎ K Q J 9 8
```

_Smashing!_

## Making an Executable

On Unix systems, a shebang (`#!`) indicates how a script should be interpreted. In our case, the shebang line at the top of `bridge.swift` tells the system to run the file using the `sh` subcommand of the `swift` command (`/usr/bin/swift`):

```
#!/usr/bin/swift sh
```

Doing so allows you to take the extra step to make a Swift script look and act just like a binary executable. Use `mv` to strip the `.swift` extension and `chmod` to add executable (`+x`) permissions.

```
$ mv bridge.swift bridge
$ chmod +x bridge
$ ./bridge
```

Talking the talk of a command-line program is fine for scripts on your local environment. But if you have any ambitions to share your script outside your system, a much better option would be to distribute a package instead.

## Converting Scripts to Packages

Just as Xcode Playgrounds can be a great place to try out ideas before them into an iOS or macOS app, scripts offer a lightweight alternative to creating a Swift package from the start when prototyping functionality.

`swift-sh` streamlines the conversion from script to package with its built-in `eject` command. Similar to [ejecting from a `create-react-app` setup](https://github.com/facebook/create-react-app/blob/master/packages/react-scripts/template/README.md#npm-run-eject), running `swift sh eject` copies over the underlying package structure of your script.

```
$ swift sh eject ./bridge
Created Bridge/

$ tree Bridge/
Bridge/
├── Package.swift
└── Sources
    └── main.swift
```

From here, it’s a piece of cake to [distribute your Swift executable with Homebrew](https://nshipster.com/homebrew/).

## Current Limitations

As a very early release, it’s expected for there to be a few rough edges and missing features. Here are some important details to keep in mind as you’re getting started with `swift-sh`:

### ~~Dependency on GitHub~~

~~Imported dependencies can correspond to only GitHub repositories. There’s currently no way to specify other remote or local locations. We expect this to be added in a future release.~~

This is now supported in the latest version.

```
import Remote // https://example.com/Remote.git
```

### ~~Module Names Must Match Repository Names~~

~~`swift-sh` requires module names to match the name of their repository. In many cases, this isn’t a problem because projects typically have descriptive names. However, in our example, the `DeckOfPlayingCards` module was provided by the repository [apple/example-package-deckofplayingcards](https://github.com/apple/example-package-deckofplayingcards).~~

You can now do this in the latest version.

```
import DeckOfPlayingCards // apple/example-package-deckofplayingcards == master
```

### Lack of Support for Import Declaration Syntax

As described in [last week’s article](https://nshipster.com/import/), Swift provides special syntax for importing individual declarations from external modules.

In our example, we import the [Cycle](https://github.com/NSHipster/Cycle) package to access its `cycle()` function, which is used to iterate over the players during the initial deal repeatedly.

In a conventional Swift package setup, we could import that function only. However, that syntax isn’t yet supported by `swift-sh`.

```
// 🔮 Possible Future Syntax
import func Cycle.cycle() // @NSHipster/Cycle
```

Until full support for import declaration syntax is added, you’ll only be able to import external modules in their entirety.

---

Given the importance of this functionality, we think `swift-sh` is destined to become part of the language. As momentum and excitement build around this project, keep an eye out in the [Swift forums](https://forums.swift.org) for proposals to incorporate this as a language feature in a future release.
