from gi.repository import Gtk

from .base import Widget


class NumberInput(Widget):
    def create(self):
        self.native = Gtk.SpinButton()
        self.native.set_numeric(True)
        self.native.interface = self.interface

        self.rehint()

    def set_adjustment_value(self):
        adjustment = Gtk.Adjustment(0, self.interface.min_value,
                                        self.interface.max_value,
                                        self.interface.step, 10, 0)
        self.native.set_adjustment(adjustment)


    def set_readonly(self, value):
        self.native.set_property('editable', not value)

    def set_step(self, step):
        if step:
            self.native.set_increments(step,step)

    def set_range(self, max_val, min_val):
        if max_value and min_value:
            self.native.set_range(min_value,max_value)

    def set_min_value(self, value):
        # self.native.set_range(min=value)
        pass

    def set_max_value(self, value):
        # self.native.set_range(max=value)
        pass

    def set_value(self, value):
        self.native.set_value(value)

    def set_alignment(self, value):
        if value == 'left':
            self.native.set_alignment(0)
        elif value == 'right':
            self.native.set_alignment(1)
        else:
            try:
                float(value) >=0.0 and float(value) <=1.0
                self.native.set_alignment(float(value))
            except (RuntimeError, TypeError, NameError):
                pass

    def set_font(self, value):
        if value:
            self.native.modify_font(value._impl.native)

    def rehint(self):
        self.interface.style.min_width = self.interface.MIN_WIDTH
        self.interface.style.height = 32

    def set_on_change(self, handler):
        # No special handling required.
        pass
