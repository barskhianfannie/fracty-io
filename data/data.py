import pandas as pd
import seaborn as sns
import matplotlib

df = pd.read_csv('data/pre.csv')
df_post = pd.read_csv('data/post.csv')

df_no = df[df['Sentiment'] != 'No, seems too risky.']

df_no = df_no[df_no['Sentiment'] != 'I don\'t know much about it to decide.']
df_no = df_no[df_no['Sentiment'] != 'I have no idea what that is.']

print(df_no)
df_stats = df.groupby(['Sentiment', 'Amount']).size().reset_index(name='counts')

# print(df_stats)
sns.set(font_scale = 14)
sns.set_theme(style="darkgrid")
# ax=sns.countplot(x='Status', hue='Amount', data=df)
# fig, ax = matplotlib.pyplot.subplots(figsize=(12,12.5))
ax=sns.countplot(x='Sentiment', hue='Amount', data=df_no)

ax.set_xticklabels(['Yes, if the tax laws made sense.', 'Yes'])
# ax.tick_params(axis='x', rotation=45)
# ax.set_xlabel('Blockchain Knowledge')
ax.set_title('Monthly Investment Amounts: \n Blockchain Native Investors vs. Investors w. No Blockchain Experience')
ax.legend(title='Amount (USD$)', labels=['1,000-10,000', '0-1,000', '10,000+'])
# fig = ax.get_figure()
fig2=ax.get_figure()
# ax.set_title('Survey Results : Homeowner vs. Sentiment')
# fig.savefig('prestats.png')
fig2.savefig('pre_sentiment_yes.png')
