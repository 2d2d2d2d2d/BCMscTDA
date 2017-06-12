import scTDA


t = scTDA.TopologicalRepresentation('trial4', lens='pca', metric='euclidean')
t.save('trial4', 25, 0.4);


c = scTDA.RootedGraph('trial4', 'trial4.all.tsv', groups=False)
# # c.show_statistics()
c.draw('Gm28551')
c.draw('_CDR')
c.plot_CDR_correlation()
c.plot_rootlane_correlation()