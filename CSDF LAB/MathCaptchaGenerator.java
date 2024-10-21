import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.Random;

public class MathCaptchaGenerator {
    private static final int WIDTH = 300;
    private static final int HEIGHT = 100;
    private static final int FONT_SIZE = 40;
    
    private static final Random RANDOM = new Random();

    public static void main(String[] args) {
        // Generate CAPTCHA expression and its answer
        CaptchaData captchaData = generateCaptchaData();

        // Create CAPTCHA image
        BufferedImage captchaImage = createCaptchaImage(captchaData.getExpression());

        // Display CAPTCHA image
        displayCaptchaImage(captchaImage);

        // User input simulation (for demo purposes)
        String userInput = JOptionPane.showInputDialog("Solve the CAPTCHA: " + captchaData.getExpression());

        // Verify CAPTCHA
        if (verifyCaptcha(captchaData.getAnswer(), userInput)) {
            JOptionPane.showMessageDialog(null, "CAPTCHA verified successfully!");
        } else {
            JOptionPane.showMessageDialog(null, "CAPTCHA verification failed.");
        }
    }

    private static CaptchaData generateCaptchaData() {
        int num1 = RANDOM.nextInt(50) + 1; // Random number between 1 and 50
        int num2 = RANDOM.nextInt(50) + 1; // Random number between 1 and 50
        int operator = RANDOM.nextInt(2); // 0 for addition, 1 for subtraction

        String expression;
        int answer;

        if (operator == 0) { // Addition
            expression = num1 + " + " + num2;
            answer = num1 + num2;
        } else { // Subtraction
            expression = num1 + " - " + num2;
            answer = num1 - num2;
        }

        return new CaptchaData(expression, String.valueOf(answer));
    }

    private static BufferedImage createCaptchaImage(String expression) {
        BufferedImage image = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_RGB);
        Graphics2D g = image.createGraphics();
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, WIDTH, HEIGHT);
        g.setFont(new Font("Arial", Font.BOLD, FONT_SIZE));
        g.setColor(Color.BLACK);
        g.drawString(expression, 50, 60);
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

    private static boolean verifyCaptcha(String correctAnswer, String userInput) {
        return correctAnswer.equals(userInput);
    }

    private static class CaptchaData {
        private final String expression;
        private final String answer;

        public CaptchaData(String expression, String answer) {
            this.expression = expression;
            this.answer = answer;
        }

        public String getExpression() {
            return expression;
        }

        public String getAnswer() {
            return answer;
        }
    }
}

