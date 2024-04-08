import matplotlib.pyplot as plt

from multisynth.phantoms.CirclePhantomSample import CirclePhantomSample


class PlotUtils:
    """
    A utility class for plotting stuff.
    """

    @staticmethod
    def plotCirclePhantom(circle_phantom):
        """
        Plots a circle phantom, hence, a bunch of circles.

        Parameters:
        - circle_phantom (list): A list of circles in the format [(x, y, radius), ...].

        Returns:
        - None
        """
        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Circle Phantom")
        for circle in circle_phantom.circles:
            circle_patch = plt.Circle((circle[0], circle[1]), circle[2], fill=False)
            ax.add_patch(circle_patch)
        plt.show()

    @staticmethod
    def plotCirclePhantomSample(cps:CirclePhantomSample):
        """
        Plots a circle phantom sample.

        Args:
            circle_phantom_sample (list): List of circles in the format [(x, y, radius), ...].

        Returns:
            None
        """
        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Circle Phantom Sample")
        
        for rlc in cps.rlcs:
            circle_patch = plt.Circle((rlc.x, rlc.y), rlc.radius, fill=True, color=rlc.color)
            ax.add_patch(circle_patch)

        for cc in cps.ccs:
            circle_patch = plt.Circle((cc.x, cc.y), cc.radius, fill=True, color=cc.color)
            ax.add_patch(circle_patch)

        for lc1 in cps.lc1s:
            circle_patch = plt.Circle((lc1.x, lc1.y), lc1.radius, fill=True, color=lc1.color)
            ax.add_patch(circle_patch)

        for lc2 in cps.lc2s:
            circle_patch = plt.Circle((lc2.x, lc2.y), lc2.radius, fill=True, color=lc2.color)
            ax.add_patch(circle_patch)

        for nc in cps.ncs:
            circle_patch = plt.Circle((nc.x, nc.y), nc.radius, fill=True, color=nc.color)
            ax.add_patch(circle_patch)

        for lwc in cps.lwcs:
            circle_patch = plt.Circle((lwc.x, lwc.y), lwc.radius, fill=True, color=lwc.color)
            ax.add_patch(circle_patch)

        plt.show()

