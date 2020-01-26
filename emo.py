webcam = Webcam.getDefault();
webcam.open();
try {
  ImageIO.write(webcam.getImage(), "PNG", new File("test.png"));
} catch (IOException e) {
  e.printStackTRace();
} finally {
  webcam.close();
}
