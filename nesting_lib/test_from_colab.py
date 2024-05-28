from rectpack import newPacker, PackingBin, PackingMode, GuillotineBlsfMinas, SkylineBl
import matplotlib.pyplot as plt
import matplotlib.patches as patches

rectangles = [(100, 30), (40, 60), (30, 30),(70, 70), (100, 50), (30, 30)]
bins = (200, 150)

packer_max = newPacker(mode=PackingMode.Offline, bin_algo=PackingBin.Global, rotation=False)
packer_gui = newPacker(mode=PackingMode.Offline, bin_algo=PackingBin.Global, rotation=False, pack_algo=GuillotineBlsfMinas)
packer_sky = newPacker(mode=PackingMode.Offline, bin_algo=PackingBin.Global, rotation=False, )

packers = [packer_max, packer_gui, packer_sky]

for packer in packers:
  # Add the rectangles to packing queue
  for r in rectangles:
    packer.add_rect(*r)

  # Add the bins where the rectangles will be placed
  packer.add_bin(*bins)

  # Start packing
  packer.pack()

  def plot_bin_packing(rectangles, bin):
      bin_width, bin_height = bin
      fig, ax = plt.subplots(figsize=(bin_width/10, bin_height/10))

      for rect in rectangles:
          count, x, y, width, height, bin = rect
          ax.add_patch(patches.Rectangle((x, y), width, height, edgecolor='red', facecolor='blue'))

      ax.set_xlim(0, bin_width)
      ax.set_ylim(0, bin_height)
      ax.set_aspect('equal', 'box')
      plt.xlabel('Width')
      plt.ylabel('Height')
      plt.title('Bin Packing')
      plt.grid(False)
      plt.show()


DATA = packer.rect_list()
# bin_count, rect.x, rect.y, rect.width, rect.height, rect.rid
for i in DATA: print(i);

plot_bin_packing(packer.rect_list(), bins);
