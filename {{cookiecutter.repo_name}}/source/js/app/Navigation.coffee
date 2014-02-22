# Navigation.coffee
root = exports ? this

class Navigation

    log: (msg) ->
        alert "Nav Says" + msg

unless root.Navigation
  root.Navigation = Navigation
