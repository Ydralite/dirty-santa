def animation(filename,AGENTS_PATH, standings, player_df):
    import collections 
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.animation import FuncAnimation
    from matplotlib import animation
    import psutil
    from os.path import join
    def my_function(i):
        # get data
        # clear axis
        ax.cla()
        #ax1.cla()
        # plot iteration
        toplot[i].plot(kind='bar')
        ax.set_ylim(0,4.2)
        ax.set_title('Game Output')        
        plt.xticks(rotation = 0)
    # start collections with zeros
    # define and adjust figure
    toplot = standings.cumsum(axis=1).div(standings.columns.values+1, axis=1).copy()
    toplot.index = [agent.replace('.py','') for agent in player_df['filename'].values]
    fig ,ax = plt.subplots(figsize=(16,6), facecolor='#DEDEDE')
    ax.set_facecolor('#DEDEDE')
    ax.set_title('Game Output')
    plt.xticks(rotation = 0)
    # animate
    ani = FuncAnimation(fig, my_function, frames = toplot.columns, interval=1000)
    f = r"{}.gif".format(filename) 
    writergif = animation.PillowWriter(fps=5) 
    ani.save(join(AGENTS_PATH, 'animations\\' , f), writer=writergif)