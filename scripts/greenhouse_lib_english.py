#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Thomas Kaulke, kaulketh@gmail.com

empty = ' '

# commands and descriptions
panic = 'Panic'
cancel = 'Cancel'
all = 'All'
stop = 'Stop'
group1 = ('Tomatoes', 'Tomatoes 1', 'Tomatoes 2', 'Tomatoes 3')
group2 = ('Chilis', 'Chili 1', 'Chili 2', 'Chili 3')
group3 = ('Reserve', 'Reserve 1', 'Reserve 2')

# messages
msg_welcome = '`Welcome {}, let us water plants!\n`'
msg_stop = '`Allright, bye til next time, {}!\nStart next watering with /start`'
msg_duration = '`Please enter duration for watering of \'{}\' in seconds:`'
water_on = '`\'{}\' will watered for {}s now.`'
water_on_group = '`All {} will now watered for {}s.`'
water_on_all = '`{} will now watered for {}s.`'
water_off = '`Watering of \'{}\' after {}s finished.\n\n`'
water_off_group = '`Watering of all {} was finished after {}s.\n\n`'
water_off_all = '`Complete watering finished after {}s.`\n\n'
msg_choice = '`Please select:`'
msg_new_choice = '`New choice or stop?`'
msg_panic = '*Panic called! \nTry some special!*'
private_warning = '`Hello {}, this is a private Bot!\nYour ChatID: {} has been blocked.`'