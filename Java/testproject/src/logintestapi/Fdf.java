package logintestapi;

import java.util.Random;

public class Fdf {

	public static void main(String[] args) {

		String str1 = "orderId=123123;customId=417;addersId=987898";

		String str2 = "orderId=123456customId=417addersId=987898";

		String returnStr = null;

		Random rm = new Random();

		int i = rm.nextInt(2);

		if (i == 0) {

			returnStr = str1;

		} else {

			returnStr = str2;
		}
		System.out.println("实际返回" + returnStr);

		String order = returnStr.substring(returnStr.indexOf("orderId="), returnStr.indexOf("customId"));
		System.out.println("截取" + order);
		if (order.contains(";")) {
			System.out.println("ture " + order);
			String t[] = order.split("=");
			String s[] = t[1].split(";");
			System.out.println("正确" + s[0]);

		} else {
			System.out.println("F " + order);
			String r[] = order.split("=");
			System.out.println("错误" + r[1]);

		}

		// String str = "orderId=123456customId=417addersId=987898";
		// // String strs[] = str.split(";");
		// // System.out.println(strs[1]);
		// // String order = strs[1];
		// //
		// // String or[] = order.split("=");
		// // System.out.println(or[1]);
		//
		// String order = str.substring(str.indexOf("orderId="),
		// str.indexOf("customId"));
		// String or[] = order.split("=");
		// System.out.println(or[1]);

		// int numberint = 0;
		// int zong = 0;
		// numberint = sum(100);
		// zong = sum(numberint);
		// // System.out.println(zong);
	}

	public static int sum(int m) {

		int sumint = 0;
		for (int i = 0; i <= m; i++) {
			sumint = sumint + i;
		}

		return sumint;
	}

	// public static void sum(int m) {
	// int sum = 0;
	// int i = 0;
	// // int j = 0;
	// for (i = 0; i <= m; i++) {
	// sum = sum + i;
	// }
	//
	// // for (j = 0; j <= 100; j++) {
	// // if (j % 2 != 0) {
	// // System.out.println("j is " + j);
	// // }
	// // }
	//
	// System.out.println(sum);
	// }

}

// @Test
// public class login {
// public void f() {
// System.out.println("代码开始");
// // 调用Chrome浏览器
// System.setProperty("webdriver.chrome.driver", "E:\\chromedriver.exe");
// // 模拟手机模式
// Map<String, String> mobileEmulation = new HashMap<String, String>();
// mobileEmulation.put("deviceName", "Google Nexus 5");
// Map<String, Object> chromeOptions = new HashMap<String, Object>();
// chromeOptions.put("mobileEmulation", mobileEmulation);
// DesiredCapabilities capabilities = DesiredCapabilities.chrome();
// capabilities.setCapability(ChromeOptions.CAPABILITY, chromeOptions);
// WebDriver driverchrome = new ChromeDriver();
// // 打开网站
//
// try {
// driverchrome.get("https://m.228.cn");
// Thread.sleep(5);
// } catch (InterruptedException e) {
// // TODO Auto-generated catch block
// e.printStackTrace();
// }
// driverchrome.findElement(By.xpath("//*[@id=\"app\"]/div[5]/ul/li[2]/a")).click();
// driverchrome.findElement(By.name("loginname")).sendKeys("15810318261");
// driverchrome.findElement(By.name("loginpwd")).sendKeys("123456");
// driverchrome.findElement(By.id("loginbtn")).click();
//
// // driverchrome.quit();
// // d调用Firefox浏览器
// // System.setProperty("webdriver.firefox.marionette", "C:\\Program Files
// // (x86)\\Mozilla Firefox\\firefox.exe");
// // WebDriver dirverfix = new FirefoxDriver();
// // dirverfix.get("http://www.baidu.com");
// // dirverfix.quit();
// }
//
// @BeforeTest
// public void beforeTest() {
// System.out.println("beforeTEst");
//
//
//
//
// }
//
// @AfterTest
// public void afterTest() {
// System.out.println("afterTEst");
// }
//
// }
