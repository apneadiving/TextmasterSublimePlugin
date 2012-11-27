# Sublime Text 2 plugin: Textmaster Framework



## Shortcut Keys

**OSX:**

 * `CTRL+J` - Create JS Framework files
 * `SHIFT+CTRL+J` - Create JS Framework files

Type `client_area/index` and which creates `app/assets/javascripts/src/pages/client_area/index` with two files:

`controller.coffee`

```coffeescript
#= require './view'
module = Textmaster.Client.Area.Index

class module.Controller extends Framework.Controller
 @options {
   View: module.View
     events:
       'event_name': { el: 'elt_name', type: 'click' }
 }
```

`view.coffee`

```coffeescript
module = Textmaster.Client.Area.Index

class module.View extends Framework.View
 @options {
   selectors:
     your_selector:
}
```

## Installation

### Git

This method required a little more work, but simply clone this repo into your Sublime Text 2 Package directory.

    $ git clone git@github.com:apneadiving/TexmasterFramework.git

