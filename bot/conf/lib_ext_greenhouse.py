#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Thomas Kaulke"
__email__ = "kaulketh@gmail.com"

from .access import token, thk
from .lib_global import line_break, commit_id, bot_dir, bot_backup

newline = line_break
cmd_prefix = '/'
cmd_restart = '{0}RESTART'.format(cmd_prefix)
cmd_update = '{0}UPDATE'.format(cmd_prefix)
cmd_logrotate = '{0}LOG_ROTATE'.format(cmd_prefix)
cmd_help = '{0}help'.format(cmd_prefix)
cmd_all_on = '{0}all_on'.format(cmd_prefix)
cmd_all_off = '{0}all_off'.format(cmd_prefix)
cmd_group1_on = '{0}group1_on'.format(cmd_prefix)
cmd_group1_off = '{0}group1_off'.format(cmd_prefix)
cmd_group2_on = '{0}group2_on'.format(cmd_prefix)
cmd_group2_off = '{0}group2_off'.format(cmd_prefix)
cmd_group3_on = '{0}group3_on'.format(cmd_prefix)
cmd_group3_off = '{0}group3_off'.format(cmd_prefix)
cmd_live = '{0}live'.format(cmd_prefix)
cmd_kill = '{0}kill'.format(cmd_prefix)

msg_help = 'Usage and possible commands in special mode:{0}' \
           '{1} - this info{0}' \
           '{2} - restart the whole RSBPi{0}' \
           '{3} - force update from repository{0}' \
           '{4} - force archiving and cleaning of log files{0}' \
           '{5} - stop this mode{0}' \
           '{6} - switch all on{0}' \
           '{7} - switch all off{0}' \
           '{8} - switch group 1 on{0}' \
           '{9} - switch group 1 off{0}' \
           '{10} - switch group 2 on{0}' \
           '{11} - switch group 2 off{0}' \
           '{12} - switch group 3 on{0}' \
           '{13} - switch group 3 off{0}' \
           '{14} - Live stream'\
    .format(newline,
            cmd_help, cmd_restart, cmd_update, cmd_logrotate, cmd_kill,
            cmd_all_on, cmd_all_off, cmd_group1_on, cmd_group1_off, cmd_group2_on,
            cmd_group2_off, cmd_group3_on, cmd_group3_off, cmd_live)

msg_unknown = 'Unknown in this mode...!\nPlease use /help for more information.'
msg_update = 'Update forced manually, info is available in separate log file.'


tmp_file = 'cmd.tmp'
del_tmp = 'rm -r ' + tmp_file

get_pid1 = 'ps -o pid,args -C python | awk \'/greenhouse.py/ { print $1 }\''
get_pid2 = 'ps -o pid,args -C python | awk \'/ext_greenhouse.py/ { print $1 }\''

restart_bot = 'python ' + str(bot_dir) + 'greenhouse.py &'

update_bot = 'rm '+ str(commit_id) + ' && bash ' + str(bot_dir) + 'update_bot.sh ' \
             + str(token) + ' ' + str(thk) + ' &'

backup_all = 'tar -zcf ' + str(bot_backup) + ' --exclude=\'*.pyc\' ' + str(bot_dir) + ' &'
logrotate_bot = 'logrotate -f /etc/logrotate.conf &'


if __name__ == '__main__':
    pass
