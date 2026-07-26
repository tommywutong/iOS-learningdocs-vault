---
title: WorkoutKit
framework: WorkoutKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/workoutkit
source_url: 'https://developer.apple.com/documentation/workoutkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/workoutkit.json'
content_hash: 'sha256:a2575705fc342292'
translated: false
---

> Navigation: [Technologies](technologies.md)

# WorkoutKit

<sub>Framework</sub>

Create, preview, and sync workout compositions to the Workout app.

## Overview

The WorkoutKit framework provides models and utilities for creating and previewing workouts in your iOS and watchOS apps, and for syncing scheduled workouts to the Workout app on Apple Watch. The framework supports the following types of workouts:

- **[CustomWorkout](workoutkit/customworkout.md)** — A structured interval workout with a series of steps containing custom goals and alerts
- **[SingleGoalWorkout](workoutkit/singlegoalworkout.md)** — A workout with a single goal, such as distance, energy, or time
- **[PacerWorkout](workoutkit/pacerworkout.md)** — A workout with distance and time goals
- **[SwimBikeRunWorkout](workoutkit/swimbikerunworkout.md)** — A workout that allows triathletes to seamlessly transition between swim, bike, and run activities

You define a workout by initializing one of these workout types. Then you use the workout to create a [WorkoutPlan](workoutkit/workoutplan.md), which provides methods for previewing, syncing, or exporting the plan. To open the plan in Workout on Apple Watch, call [openInWorkoutApp()](<workoutkit/workoutplan/openinworkoutapp().md>). To export the plan, call the `dataRepresentation(as:)` method.

You can also use WorkoutKit to create and maintain a workout schedule and, with the user’s permission, sync scheduled compositions to Apple Watch. These compositions appear in a dedicated space in the Workout app and include your app’s icon and name.

Before you can schedule a workout, you must ask for permission. Get the shared [WorkoutScheduler](workoutkit/workoutscheduler.md) instance, and call its [requestAuthorization()](<workoutkit/workoutscheduler/requestauthorization().md>) method. Then call the [schedule(_:at:)](<workoutkit/workoutscheduler/schedule(__at_).md>) method to schedule workouts.

To access health data for the workout, see the [HealthKit](healthkit.md) framework.

## Topics

### Essentials

- [Customizing workouts with WorkoutKit](workoutkit/customizing-workouts-with-workoutkit.md) — Create, preview, and sync workouts for use in the Workout app on Apple Watch.

### Common workouts

- [SingleGoalWorkout](workoutkit/singlegoalworkout.md) — A workout with a single goal.
- [PacerWorkout](workoutkit/pacerworkout.md) — A workout in which a person covers a specific distance in a given time.
- [SwimBikeRunWorkout](workoutkit/swimbikerunworkout.md) — A workout for multisport activities that include running, biking, and swimming.

### Custom interval workouts

- [CustomWorkout](workoutkit/customworkout.md) — A workout that includes a repeating series of work and recovery steps.
- [WorkoutStep](workoutkit/workoutstep.md) — A step in a workout.
- [IntervalBlock](workoutkit/intervalblock.md) — Blocks of work and recovery steps that repeat in a custom workout.
- [IntervalStep](workoutkit/intervalstep.md) — An interval that represents a work or recovery step in a workout.
- [WorkoutGoal](workoutkit/workoutgoal.md) — A value that specifies the goal for a workout.
- [WorkoutAlert](workoutkit/workoutalert.md) — An alert that notifies the user of significant events during a workout.

### Workout plans and schedules

- [WorkoutPlan](workoutkit/workoutplan.md) — A wrapper around a workout object that your app can use to open the object in Workout or schedule it for later.
- [ScheduledWorkoutPlan](workoutkit/scheduledworkoutplan.md) — A wrapper around a workout plan that your app can use to schedule the workout plan.
- [WorkoutScheduler](workoutkit/workoutscheduler.md) — An object for scheduling and managing workouts.

### Errors

- [StateError](workoutkit/stateerror.md) — An error that occurs while previewing a workout composition.
