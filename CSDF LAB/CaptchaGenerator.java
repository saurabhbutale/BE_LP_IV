import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.Random;

public class CaptchaGenerator {
    private static final int WIDTH = 150;
    private static final int HEIGHT = 50;
    private static final int FONT_SIZE = 30;
    private static final int CAPTCHA_LENGTH = 6;
    private static final String CHAR_POOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    public static void main(String[] args) {
        // Generate CAPTCHA image
        String captchaText = generateCaptchaText();
        BufferedImage captchaImage = createCaptchaImage(captchaText);

        // Display CAPTCHA image
        displayCaptchaImage(captchaImage);

        // User input simulation (for demo purposes)
        String userInput = JOptionPane.showInputDialog("Enter the CAPTCHA text:");

        // Verify CAPTCHA
        if (verifyCaptcha(captchaText, userInput)) {
            JOptionPane.showMessageDialog(null, "CAPTCHA verified successfully!");
        } else {
            JOptionPane.showMessageDialog(null, "CAPTCHA verification failed.");
        }
    }

    private static String generateCaptchaText() {
        Random random = new Random();
        StringBuilder captcha = new StringBuilder(CAPTCHA_LENGTH);
        for (int i = 0; i < CAPTCHA_LENGTH; i++) {
            captcha.append(CHAR_POOL.charAt(random.nextInt(CHAR_POOL.length())));
        }
        return captcha.toString();
    }

    private static BufferedImage createCaptchaImage(String captchaText) {
        BufferedImage image = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_RGB);
        Graphics2D g = image.createGraphics();
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, WIDTH, HEIGHT);
        g.setFont(new Font("Arial", Font.BOLD, FONT_SIZE));
        g.setColor(Color.BLACK);
        g.drawString(captchaText, 20, 35);
        g.dispose();

        return image;
    }

    private static void displayCaptchaImage(BufferedImage captchaImage) {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(WIDTH + 20, HEIGHT + 40);

        JLabel label = new JLabel(new ImageIcon(captchaImage));
        frame.getContentPane().add(label);
        frame.setVisible(true);
    }

    private static boolean verifyCaptcha(String originalText, String userInput) {
        return originalText.equals(userInput);
    }
}

