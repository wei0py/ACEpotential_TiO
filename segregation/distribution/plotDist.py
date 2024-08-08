import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.patches as  mpatches

def plot_labels_new(tilts, df):

    df_new = df.copy()
    df_new = df_new[df_new["msd"]< 0.1]
    df_new["system_use"] = df_new["System"].str.split("_").str[:-2].str.join('_')
    df_new["min_segE_new"] = df_new.groupby(["system_use", "axis"])["segE_new"].transform('min')
    colors_list = ["blue", "orange", "green"]
    fig, axes = plt.subplots(1, 3, figsize=(8, 6), sharey=True, dpi = 300)
#    plt.figure(dpi = 300, figsize= (6, 4))
#    sns.kdeplot(df_new, x="min_segE_new", y="angles", fill=True, alpha=0.3,  hue = "axis",legend=True)
    for i in range(len(tilts)):
#        plt.figure(dpi = 300, figsize= (6, 4))
        sns.histplot(df_new[df_new["axis"]==tilts[i]]["min_segE_new"], bins = 20, kde=False, alpha=0.3, label = tilts[i], color = colors_list[i], ax = axes[i])
        axes[i].set_xlabel('Segregation Energy (eV)')
        axes[i].set_ylim(0, 6000)
        axes[i].legend()
#        axes[i].set_ylabel('Frequency')
        #sns.kdeplot(x=df_new[df_new["axis"]==tilts[i]]["min_segE_new"], y=df_new[df_new["axis"]==tilts[i]]["angles"], fill=True, alpha=0.3, label = tilts[i], legend = True)
    # Adjust layout
        #handles = [mpatches.Patch(facecolor=plt.cm.Blues(100), label=tilts[0]),
        #   mpatches.Patch(facecolor=plt.cm.Oranges(100), label=tilts[1]),
        #   mpatches.Patch(facecolor=plt.cm.Greens(100), label=tilts[2])] 
     #plt.legend(handles = handles)
 #       plt.xlabel("Segregation Energy (eV)")
    #plt.ylabel("Angles")
    plt.tight_layout()    
    plt.savefig("labels_dis_min0.1_sep.png")

def plot_labels(tilts, df):
    df = df[df["msd"]< 0.1]
    plt.figure(dpi = 300, figsize = (8, 6))
    for i in range(len(tilts)):
        sns.histplot(df[df["axis"]==tilts[i]]["segE_new"], bins = 20, kde=True, alpha=0.3, label = tilts[i])
    # Adjust layout
    
    plt.legend()
    plt.xlabel("Segregation Energy (eV)")
    plt.tight_layout()    
    plt.savefig("labels0.1.png")

def plot_msd(tilts, df):
    plt.figure(dpi = 300)
    for i in range(len(tilts)):
        sns.histplot(df[df["axis"]==tilts[i]]["msd"], bins = 20, kde=True, alpha=0.3, label = tilts[i])
    # Adjust layout

    plt.legend()
    plt.xlabel("Total Displacement ($\AA$)")
    plt.tight_layout()
    plt.savefig("Meanmsd_distri.png")

def plot(df):
    plt.figure(dpi = 300)
    ax2 = df.plot.scatter(x='segE_new',
                       y='msd',
                      c='numA',
                      alpha = 0.5,
                      colormap='viridis')
    plt.savefig("msd.png")

df = pd.read_csv("msd_merge.csv")
print(len(df[df["segE_new"]<0])/len(df))
print(len(df[df["msd"]<0.1]))
#print(df[df["segE_new"]>2].loc[:, ["System", "segE_new"]])
plot_labels_new(["0001","01-10","12-10"], df)
plot_labels(["0001","01-10","12-10"], df)
#plot_msd(["0001","01-10","12-10"], df)
# plot(df)
