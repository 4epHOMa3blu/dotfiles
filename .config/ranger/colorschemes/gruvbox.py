from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

light_red = 160
light_orange = 172
light_yellow = 220
light_green = 148
light_cyan = 117
light_blue = 31
light_magenta = 133
light_fg = 230
light_bg = 236

dark_red = 124
dark_orange = 130
dark_yellow = 178
dark_green = 106
dark_cyan = 74
dark_blue = 25
dark_magenta = 127
dark_fg = 187
dark_bg = 235

class LightGruvbox(ColorScheme):
    progress_bar_color = 108

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            if context.selected:
                attr = reverse
            else:
                attr = normal
            if context.empty or context.error:
                fg = light_red
            if context.border:
                fg = light_yellow
            if context.image:
                fg = light_cyan
            if context.video:
                fg = dark_cyan
            if context.audio:
                fg = light_orange
            if context.document:
                fg = light_green
            if context.container:
                attr |= bold
                fg = dark_yellow
            if context.directory:
                attr |= bold
                fg = dark_yellow
            elif context.executable and not \
                    any((context.media, context.container,
                       context.fifo, context.socket)):
                fg = light_orange
            if context.socket:
                fg = light_blue
                attr |= bold
            if context.fifo or context.device:
                fg = light_cyan
                if context.device:
                    attr |= bold
                    fg = light_cyan

            if context.link:
                fg = context.good and 223 or 116
                bg = 234
            if context.bad:
                bg = 235
            if context.tag_marker and not context.selected:
                attr |= bold
                if fg in (174, 95):
                    fg = 248
                else:
                    fg = 174
            if not context.selected and (context.cut or context.copied):
                fg = 108
                bg = 234

            if context.main_column:
                if context.selected:
                    attr |= bold
                if context.marked:
                    attr |= bold
                    fg = 223
            if context.badinfo:
                if attr & reverse:
                    bg = 95
                else:
                    fg = 95

        elif context.in_titlebar:
            attr |= bold
            if context.hostname:
                fg = context.bad and dark_magenta or light_magenta
            elif context.directory:
                fg = light_orange
            elif context.tab:
                if context.good:
                    bg = light_fg
            elif context.link:
                fg = light_cyan

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = dark_cyan
                elif context.bad:
                    fg = dark_magenta
            if context.marked:
                attr |= bold | reverse
                fg = light_fg
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = dark_magenta
            if context.loaded:
                bg = light_green
            if context.vcsinfo:
                fg = dark_cyan
                attr &= ~bold
            if context.vcscommit:
                fg = light_blue
                attr &= ~bold


        if context.text:
            if context.highlight:
                attr |= reverse
                fg = light_fg

        if context.in_taskview:
            if context.title:
                fg = light_cyan

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    bg = self.progress_bar_color


        if context.vcsfile and not context.selected:
            attr &= ~bold
            if context.vcsconflict:
                fg = light_red
            elif context.vcschanged:
                fg = light_green
            elif context.vcsunknown:
                fg = light_magenta
            elif context.vcsstaged:
                fg = light_cyan
            elif context.vcssync:
                fg = light_cyan
            elif context.vcsignored:
                fg = light_fg

        elif context.vcsremote and not context.selected:
            attr &= ~bold
            if context.vcssync:
                fg = light_cyan
            elif context.vcsbehind:
                fg = light_magenta
            elif context.vcsahead:
                fg = light_cyan
            elif context.vcsdiverged:
                fg = light_red
            elif context.vcsunknown:
                fg = light_magenta

        return fg, bg, attr
