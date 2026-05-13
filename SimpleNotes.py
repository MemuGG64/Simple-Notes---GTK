#!/usr/bin/env python3
import sys
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(script_dir, 'src'))

if __name__ == "__main__":
    try:
        import gi
        gi.require_version('Gtk', '3.0')
        from gi.repository import Gtk
    except (ImportError, ValueError) as e:
        if sys.platform == "darwin":
            print("=" * 60)
            print("  SimpleNotes-GTK requires GTK3 and PyGObject.")
            print()
            print("  Install via Homebrew:")
            print("    brew install gtk+3 pygobject3")
            print()
            print("  Then run: python3 SimpleNotes.py")
            print("=" * 60)
        else:
            print(f"Error: GTK3 not available. {e}")
            print("Install: sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0")
        sys.exit(1)

    import main

    app = main.SimpleNotes_GTK()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()
