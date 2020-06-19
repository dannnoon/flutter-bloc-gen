# flutter-bloc-gen

Generates 4 files required for every page that is using BLoC pattern:
- Page
- Bloc
- State
- Event

Files are generated under path<br />
`./lib/presentation/<name>/`<br />
where name is argument passed as `-n` (or `--name`)<br />

## Instructions

Make sure you are running this script from you main flutter project folder (the one that contains `lib` directory)<br />
Add this script to your `PATH` for more convinient use<br />
Make this file executable (`chmod +x fbg.py`)<br />

#### Example

Running:
`fbg.py --name delayed_departure_list`
generates files:
```
\- lib
 \- presentation
  \- delayed_departure_list
   \- delayed_departure_list_page.dart
      delayed_departure_list_bloc.dart
      delayed_departure_list_state.dart
      delayed_departure_list_event.dart
```
containing initial content.
