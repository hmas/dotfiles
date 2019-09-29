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
                    ' according |{{to reports being filed with|records of}} Security Exchange Commission|{{ (SEC)|}}',
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
            
