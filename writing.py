desc = {
        '_type': 'Ranking',
        'rank': [
            {
                '_type': 'StateMachine',
                'condition': num_names > 3 and buy > 0 and sell > 0,
                'parameters': {'*': 0 if cutoff_date != '2018-01-01' else 1},
                'order': ['s1', 's1-2', 's2', 's3', 's4'],
                's1': [
                    ' '.join([
                        '{} are insiders of {} with highest number of shares being |{{bought|purchased|acquired}} from the open market'.format(names, company_name),
                        '*{{in the last {} weeks (since {})|since Jan 1th, 2018}},'.format(num_weeks, cutoff_date),
                    ]),
                    ' '.join([
                        '{} are insiders of {} that |{{bought|purchased|acquired}} most number of shares in the open market'.format(names, company_name),
                        '*{{in the last {} weeks (since {})|since Jan 1th, 2018}},'.format(num_weeks, cutoff_date),
                    ]),
                ],
                's1-2': [
                    ' according to |{{reports being filed with|records of}} Security Exchange Commission|{{ (SEC)|(www.sec.gov)|}}.',
                ]
                's2': [
                    '!{{Collectively|All together}}, insiders of {} |{{bought|purchased|acquired}} {} number of shares in the same period.'.format(company_name, buyers_collective_num_shares),
                ],
                's3': [
                    'This |{{compares with|is against}} {} shares being |{{sold|dumped}} in the exact timeframe, by the insiders |{{(and/or major shareholders)|and/or major shareholders}}.'.format(sellers_collective_num_shares),
                ],
                's4': [
                    ' '.join([
                        '|{{However, |}}it worth |{{noting|mentioning}} that |{{generally | in most cases |}}an',
                        'insider ^{{buy|acquisition}} is a |{{much |}}stronger signal comparing to a ^{{sell|disposition}} by an insider.',
                    ]),
                    ' '.join([
                        '!{{Generally, |In most situations, |In most cases, |}}!{{it|it|it|It}}',
                        'worth mentioning that|{{, however,|}} most investors consider a ^{{buy|acquisition}}',
                        'signal, by an insider, more |{{meaningful|significant|newsworthy}} comparing to a ^{{sell|disposition}} signal.',
                    ])
                ],
            },
            {
                '_type': 'StateMachine',
                'condition': float(d[_k.SHARES_QUANTITY]) >= 1000 and d[_k.ACQUIRED_OR_DISPOSED] == 'D',
                'start': '{} Dumps {} Shares of ${{{}}}'.format(nameformat(d[_k.OWNER_NAME]), sharequantityformat(d[_k.SHARES_QUANTITY]), _k.COMPANY_NAME),

            },
            {
                '_type': 'StateMachine',
                'condition': float(_total_value(d)) >= 1000000 and d[_k.ACQUIRED_OR_DISPOSED] == 'D',
                'start': '{} Sells ${{{}}} shares of ${{{}}}'.format(nameformat(d[_k.OWNER_NAME]), _k.SHARES_QUANTITY, _k.COMPANY_NAME),
            },
            {
                '_type': 'StateMachine',
                'totalvalue': total_value(d),
                'start': 'Insider Action Alert: ${{{}}}'.format(_k.COMPANY_NAME),
            },
        ],
    }
